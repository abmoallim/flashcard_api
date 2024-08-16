from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.subscription import SubscriptionCreate, SubscriptionResponse
from app.crud.subscription import get_subscription, create_subscription, get_subscriptions, delete_subscription, update_subscription
from app.db.session import get_db

router = APIRouter()

@router.post("/", response_model=SubscriptionResponse)
def create_new_subscription(subscription: SubscriptionCreate, db: Session = Depends(get_db)):
    return create_subscription(db=db, subscription=subscription)

@router.get("/{subscription_id}", response_model=SubscriptionResponse)
def read_subscription(subscription_id: int, db: Session = Depends(get_db)):
    db_subscription = get_subscription(db, subscription_id=subscription_id)
    if db_subscription is None:
        raise HTTPException(status_code=404, detail="Subscription not found")
    return db_subscription

@router.get("/", response_model=list[SubscriptionResponse])
def read_subscriptions(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    subscriptions = get_subscriptions(db, skip=skip, limit=limit)
    return subscriptions

@router.delete("/{subscription_id}", response_model=SubscriptionResponse)
def delete_existing_subscription(subscription_id: int, db: Session = Depends(get_db)):
    subscription = delete_subscription(db, subscription_id=subscription_id)
    if subscription is None:
        raise HTTPException(status_code=404, detail="Subscription not found")
    return subscription

@router.put("/{subscription_id}", response_model=SubscriptionResponse)
def update_existing_subscription(subscription_id: int, subscription: SubscriptionCreate, db: Session = Depends(get_db)):
    db_subscription = update_subscription(db, subscription_id=subscription_id, updated_subscription=subscription)
    if db_subscription is None:
        raise HTTPException(status_code=404, detail="Subscription not found")
    return db_subscription
