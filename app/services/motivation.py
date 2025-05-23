from sqlalchemy.orm import Session

def add_quote(db: Session, data):
    from app.models.motivation import Motivation
    quote = Motivation(**data.dict())
    db.add(quote)
    db.commit()
    db.refresh(quote)
    return quote

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
