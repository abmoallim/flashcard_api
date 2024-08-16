from sqlalchemy.orm import Session
from app.db.models.user import User
from app.schemas.user import UserCreate
from app.core.security import hash_password

def get_user(db: Session, user_id: str):
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(User).offset(skip).limit(limit).all()

def delete_user(db: Session, user_id: str):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
    return user

def update_user(db: Session, user_id: str, updated_user: UserCreate):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        user.email = updated_user.email
        user.hashed_password = hash_password(updated_user.password)
        user.full_name = updated_user.full_name
        db.commit()
        db.refresh(user)
    return user
