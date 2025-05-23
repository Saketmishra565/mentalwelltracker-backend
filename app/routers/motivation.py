from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas.motivation import MotivationCreate, MotivationRead, MotivationUpdate
from app.services.motivation import (
    add_quote,
    get_all_quotes,
    get_quote_by_id,
    update_quote,
    delete_quote,
)

router = APIRouter(prefix="/motivation", tags=["Motivation"])

# CREATE
@router.post("/", response_model=MotivationRead, status_code=status.HTTP_201_CREATED)
def add_motivational_quote(quote: MotivationCreate, db: Session = Depends(get_db)):
    return add_quote(db, quote)

# READ ALL
@router.get("/", response_model=List[MotivationRead])
def list_quotes(db: Session = Depends(get_db)):
    return get_all_quotes(db)

# READ BY ID
@router.get("/{quote_id}", response_model=MotivationRead)
def get_quote(quote_id: int, db: Session = Depends(get_db)):
    quote = get_quote_by_id(db, quote_id)
    if not quote:
        raise HTTPException(status_code=404, detail="Quote not found")
    return quote

# UPDATE
@router.put("/{quote_id}", response_model=MotivationRead)
def update_motivational_quote(quote_id: int, update_data: MotivationUpdate, db: Session = Depends(get_db)):
    updated = update_quote(db, quote_id, update_data)
    if not updated:
        raise HTTPException(status_code=404, detail="Quote not found")
    return updated

# DELETE
@router.delete("/{quote_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_motivational_quote(quote_id: int, db: Session = Depends(get_db)):
    deleted = delete_quote(db, quote_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Quote not found")
    return None
