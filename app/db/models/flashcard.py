from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.db.session import Base

class Flashcard(Base):
    __tablename__ = "flashcards"

    id = Column(Integer, primary_key=True, index=True)
    question = Column(String, nullable=False)
    answer = Column(String, nullable=False)
    deck_id = Column(Integer, ForeignKey("decks.id"))
    owner_id = Column(String, ForeignKey("users.id")) 

    deck = relationship("Deck", back_populates="flashcards")
    owner = relationship("User", back_populates="flashcards")  #
