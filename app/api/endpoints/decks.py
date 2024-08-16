from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.deck import DeckCreate, DeckResponse
from app.crud.deck import get_deck, create_deck, get_decks, delete_deck, update_deck
from app.db.session import get_db

router = APIRouter()

@router.post("/", response_model=DeckResponse)
def create_new_deck(deck: DeckCreate, db: Session = Depends(get_db)):
    return create_deck(db=db, deck=deck)

@router.get("/{deck_id}", response_model=DeckResponse)
def read_deck(deck_id: int, db: Session = Depends(get_db)):
    db_deck = get_deck(db, deck_id=deck_id)
    if db_deck is None:
        raise HTTPException(status_code=404, detail="Deck not found")
    return db_deck

@router.get("/", response_model=list[DeckResponse])
def read_decks(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    decks = get_decks(db, skip=skip, limit=limit)
    return decks

@router.delete("/{deck_id}", response_model=DeckResponse)
def delete_existing_deck(deck_id: int, db: Session = Depends(get_db)):
    deck = delete_deck(db, deck_id=deck_id)
    if deck is None:
        raise HTTPException(status_code=404, detail="Deck not found")
    return deck

@router.put("/{deck_id}", response_model=DeckResponse)
def update_existing_deck(deck_id: int, deck: DeckCreate, db: Session = Depends(get_db)):
    db_deck = update_deck(db, deck_id=deck_id, updated_deck=deck)
    if db_deck is None:
        raise HTTPException(status_code=404, detail="Deck not found")
    return db_deck
