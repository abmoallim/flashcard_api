from pydantic import BaseModel

class FlashcardBase(BaseModel):
    question: str
    answer: str
    deck_id: int  
    owner_id: str # Include deck_id in the schema

class FlashcardCreate(FlashcardBase):
    pass

class FlashcardResponse(FlashcardBase):
    id: int

    class Config:
        from_attributes = True
