from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.flashcard import FlashcardCreate
from app.crud.flashcard import create_flashcard
from app.db.session import get_db
import openai
import os
from pydantic import BaseModel

router = APIRouter()

# Load environment variables
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
# Define the system prompt
system_prompt = """
Assume you are a flashcards creator. Your task is to generate concise and effective flashcards based on the given topic or content. Follow these guidelines:

1. Create clear and concise questions for the front of the flashcard.
2. Provide accurate and informative answers for the back of the flashcard.
3. Focus on key concepts, definitions, facts, or relationships within the given subject.
4. Ensure that each flashcard covers a single, distinct piece of information.
5. Use simple language and avoid unnecessary jargon unless it's essential to the topic.
6. For numerical or date-based information, present it clearly and consistently.
7. If applicable, include mnemonics or memory aids to help with recall.
8. Maintain a balanced difficulty level appropriate for the intended audience.
9. When dealing with lists or multiple points, break them into separate flashcards if necessary.
10. Double-check all information for accuracy before finalizing the flashcards.

Your output should be a series of flashcards, each containing a question on the front and its corresponding answer on the back.

Return in the following JSON format:
{
    "flashcards": [
        { 
            "front": str, 
            "back": str 
        }
    ]
}
"""

class GenerateFlashcardsRequest(BaseModel):
    deck_id: int
    topic: str

@router.post("/")
async def generate_flashcards(request: GenerateFlashcardsRequest, db: Session = Depends(get_db)):
    try:
        # Generate flashcards using OpenAI
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Generate flashcards for the topic: {request.topic}"}
        ]

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
        )

        # Parse the generated flashcards
        flashcards_data = eval(response.choices[0].message.content) 

        flashcards = flashcards_data["flashcards"]

        # Store the flashcards in the database
        for flashcard in flashcards:
            flashcard_create = FlashcardCreate(
                question=flashcard["front"],
                answer=flashcard["back"],
                deck_id=request.deck_id
            )
            create_flashcard(db=db, flashcard=flashcard_create)

        return {"message": "Flashcards generated and saved successfully.", "flashcards": flashcards}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
