# app\db\models\user.py
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from app.db.session import Base

class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    full_name = Column(String, index=True)
    
    decks = relationship("Deck", back_populates="owner")
    subscriptions = relationship("Subscription", back_populates="owner")
