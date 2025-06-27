from app.models.motivation import Motivation
from sqlalchemy.orm import Session
from app.schemas.motivation import MotivationCreate

def add_quote(db: Session, quote_data: MotivationCreate, user_id: int):
    new_quote = Motivation(
        quote=quote_data.quote,
        author=quote_data.author,
        user_id=user_id
    )
    db.add(new_quote)
    db.commit()
    db.refresh(new_quote)
    return new_quote

def get_all_quotes(db: Session):
    from app.models.motivation import Motivation
    return db.query(Motivation).all()

def get_quote_by_id(db: Session, quote_id: int):
    from app.models.motivation import Motivation
    return db.query(Motivation).filter(Motivation.id == quote_id).first()

def update_quote(db: Session, quote_id: int, update_data):
    from app.models.motivation import Motivation
    quote = get_quote_by_id(db, quote_id)
    if not quote:
        return None
    for key, value in update_data.dict(exclude_unset=True).items():
        setattr(quote, key, value)
    db.commit()
    db.refresh(quote)
    return quote

def delete_quote(db: Session, quote_id: int):
    from app.models.motivation import Motivation
    quote = get_quote_by_id(db, quote_id)
    if not quote:
        return None
    db.delete(quote)
    db.commit()
    return quote
