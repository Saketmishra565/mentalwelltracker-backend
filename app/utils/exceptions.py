from fastapi import HTTPException

def raise_404(detail="Item not found"):
    raise HTTPException(status_code=404, detail=detail)
