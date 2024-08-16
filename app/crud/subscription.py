from sqlalchemy.orm import Session
from app.db.models.subscription import Subscription
from app.schemas.subscription import SubscriptionCreate

def get_subscription(db: Session, subscription_id: int):
    return db.query(Subscription).filter(Subscription.id == subscription_id).first()

def get_subscriptions(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Subscription).offset(skip).limit(limit).all()

def create_subscription(db: Session, subscription: SubscriptionCreate):
    db_subscription = Subscription(**subscription.dict())
    db.add(db_subscription)
    db.commit()
    db.refresh(db_subscription)
    return db_subscription

def delete_subscription(db: Session, subscription_id: int):
    subscription = db.query(Subscription).filter(Subscription.id == subscription_id).first()
    if subscription:
        db.delete(subscription)
        db.commit()
    return subscription

def update_subscription(db: Session, subscription_id: int, updated_subscription: SubscriptionCreate):
    subscription = db.query(Subscription).filter(Subscription.id == subscription_id).first()
    if subscription:
        subscription.status = updated_subscription.status
        subscription.plan = updated_subscription.plan
        subscription.stripe_subscription_id = updated_subscription.stripe_subscription_id
        db.commit()
        db.refresh(subscription)
    return subscription
