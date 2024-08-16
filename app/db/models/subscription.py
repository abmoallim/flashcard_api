from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.db.session import Base

class Subscription(Base):
    __tablename__ = "subscriptions"

    id = Column(Integer, primary_key=True, index=True)
    stripe_subscription_id = Column(String, nullable=False)
    status = Column(String, nullable=False)
    plan = Column(String, nullable=False)
    owner_id = Column(String, ForeignKey("users.id"))

    owner = relationship("User", back_populates="subscriptions")
