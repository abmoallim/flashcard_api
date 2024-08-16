from pydantic import BaseModel
from typing import List, Optional
from app.schemas.flashcard import FlashcardResponse  # Import the FlashcardResponse schema

from pydantic import BaseModel

class DeckCreate(BaseModel):
    name: str
    description: str
    owner_id: str  # Include owner_id in the schema

class DeckResponse(BaseModel):
    id: int
    name: str
    description: str
    owner_id: str

    class Config:
        from_attributes = True
