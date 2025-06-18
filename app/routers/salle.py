from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID
from app.schemas.salle import SalleCreate, SalleRead, SalleUpdate
from app.services.salle import get_salles, get_salle, create_salle, update_salle, delete_salle
from app.database.database import get_db

router = APIRouter(prefix="/salles", tags=["salles"])

SALLE_NOT_FOUND = "Salle non trouvée"

@router.get("/", response_model=List[SalleRead])
def list_salles(db: Session = Depends(get_db)):
    return get_salles(db)

@router.get("/{salle_id}", response_model=SalleRead)
def read_salle(salle_id: UUID, db: Session = Depends(get_db)):
    salle = get_salle(db, salle_id)
    if not salle:
        raise HTTPException(status_code=404, detail=SALLE_NOT_FOUND)
    return salle

@router.post("/", response_model=SalleRead, status_code=201)
def create_new_salle(salle: SalleCreate, db: Session = Depends(get_db)):
    return create_salle(db, salle)

@router.put("/{salle_id}", response_model=SalleRead)
def update_existing_salle(salle_id: UUID, salle: SalleUpdate, db: Session = Depends(get_db)):
    updated = update_salle(db, salle_id, salle)
    if not updated:
        raise HTTPException(status_code=404, detail=SALLE_NOT_FOUND)
    return updated

@router.delete("/{salle_id}", status_code=204)
def delete_existing_salle(salle_id: UUID, db: Session = Depends(get_db)):
    deleted = delete_salle(db, salle_id)
    if not deleted:
        raise HTTPException(status_code=404, detail=SALLE_NOT_FOUND)
    return None 