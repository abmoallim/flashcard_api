from pydantic import BaseModel

class SubscriptionBase(BaseModel):
    stripe_subscription_id: str
    status: str
    plan: str
    owner_id: str  # Include owner_id in the schema

class SubscriptionCreate(SubscriptionBase):
    pass

class SubscriptionResponse(SubscriptionBase):
    id: int

    class Config:
        from_attributes = True
