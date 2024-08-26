from sqlalchemy.orm import Session
from app.db.models.flashcard import Flashcard
from app.schemas.flashcard import FlashcardCreate
from app.db.models.deck import Deck

def get_flashcard(db: Session, flashcard_id: int):
    return db.query(Flashcard).filter(Flashcard.id == flashcard_id).first()

def get_flashcards_by_deck(db: Session, deck_id: int):
    return db.query(Flashcard).join(Deck).filter(Flashcard.deck_id == deck_id).all()

def create_flashcard(db: Session, flashcard: FlashcardCreate):
    db_flashcard = Flashcard(**flashcard.dict())
    db.add(db_flashcard)
    db.commit()
    db.refresh(db_flashcard)
    return db_flashcard

def delete_flashcard(db: Session, flashcard_id: int):
    flashcard = db.query(Flashcard).filter(Flashcard.id == flashcard_id).first()
    if flashcard:
        db.delete(flashcard)
        db.commit()
    return flashcard

def update_flashcard(db: Session, flashcard_id: int, updated_flashcard: FlashcardCreate):
    flashcard = db.query(Flashcard).filter(Flashcard.id == flashcard_id).first()
    if flashcard:
        flashcard.question = updated_flashcard.question
        flashcard.answer = updated_flashcard.answer
        flashcard.deck_id = updated_flashcard.deck_id
        db.commit()
        db.refresh(flashcard)
    return flashcard
