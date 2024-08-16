from fastapi import FastAPI
from app.api.endpoints import users, flashcards, decks, subscriptions, generate

app = FastAPI()

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(flashcards.router, prefix="/flashcards", tags=["flashcards"])
app.include_router(decks.router, prefix="/decks", tags=["decks"])
app.include_router(subscriptions.router, prefix="/subscriptions", tags=["subscriptions"])
app.include_router(generate.router, prefix="/generate", tags=["generate"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Flashcard API"}
