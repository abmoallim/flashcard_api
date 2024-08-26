from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.flashcard import FlashcardCreate, FlashcardResponse
from app.crud.flashcard import get_flashcard, create_flashcard, get_flashcards_by_deck, delete_flashcard, update_flashcard
from app.db.session import get_db

router = APIRouter()

@router.post("/", response_model=FlashcardResponse)
def create_new_flashcard(flashcard: FlashcardCreate, db: Session = Depends(get_db)):
    return create_flashcard(db=db, flashcard=flashcard)


@router.get("/{deck_id}", response_model=list[FlashcardResponse])
def read_flashcards(deck_id: int, db: Session = Depends(get_db)):
    flashcards = get_flashcards_by_deck(db, deck_id=deck_id)
    if flashcards is None:
        raise HTTPException(status_code=404, detail="Flashcards not found")
    return flashcards


# @router.get("/", response_model=list[FlashcardResponse])
# def read_flashcards( db: Session = Depends(get_db)):
#     flashcards = get_flashcards(db)
#     return flashcards

@router.delete("/{flashcard_id}", response_model=FlashcardResponse)
def delete_existing_flashcard(flashcard_id: int, db: Session = Depends(get_db)):
    flashcard = delete_flashcard(db, flashcard_id=flashcard_id)
    if flashcard is None:
        raise HTTPException(status_code=404, detail="Flashcard not found")
    return flashcard

@router.put("/{flashcard_id}", response_model=FlashcardResponse)
def update_existing_flashcard(flashcard_id: int, flashcard: FlashcardCreate, db: Session = Depends(get_db)):
    db_flashcard = update_flashcard(db, flashcard_id=flashcard_id, updated_flashcard=flashcard)
    if db_flashcard is None:
        raise HTTPException(status_code=404, detail="Flashcard not found")
    return db_flashcard
