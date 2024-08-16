from pydantic import BaseModel

class FlashcardBase(BaseModel):
    question: str
    answer: str
    deck_id: int  # Include deck_id in the schema

class FlashcardCreate(FlashcardBase):
    pass

class FlashcardResponse(FlashcardBase):
    id: int

    class Config:
        from_attributes = True
