from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.db.session import Base

class Deck(Base):
    __tablename__ = "decks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    owner_id = Column(String, ForeignKey("users.id"))

    owner = relationship("User", back_populates="decks")
    flashcards = relationship("Flashcard", back_populates="deck")
