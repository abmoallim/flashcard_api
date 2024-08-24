from sqlalchemy.orm import Session
from app.db.models.deck import Deck
from app.schemas.deck import DeckCreate

# def get_deck(db: Session, deck_id: int):
#     return db.query(Deck).filter(Deck.id == deck_id).first()

def get_user_decks(db: Session, user_id: str):
    return db.query(Deck).filter(Deck.owner_id == user_id).all()

def get_decks(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Deck).offset(skip).limit(limit).all()

def create_deck(db: Session, deck: DeckCreate):
    db_deck = Deck(**deck.dict())
    db.add(db_deck)
    db.commit()
    db.refresh(db_deck)
    return db_deck

def delete_deck(db: Session, deck_id: int):
    deck = db.query(Deck).filter(Deck.id == deck_id).first()
    if deck:
        db.delete(deck)
        db.commit()
    return deck

def update_deck(db: Session, deck_id: int, updated_deck: DeckCreate):
    deck = db.query(Deck).filter(Deck.id == deck_id).first()
    if deck:
        deck.name = updated_deck.name
        deck.description = updated_deck.description
        db.commit()
        db.refresh(deck)
    return deck
