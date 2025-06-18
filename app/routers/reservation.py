from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID
from app.schemas.reservation import ReservationCreate, ReservationRead
from app.services.reservation import get_reservations, get_reservation, create_reservation
from app.database.database import get_db

router = APIRouter(prefix="/reservations", tags=["reservations"])

@router.get("/", response_model=List[ReservationRead])
def list_reservations(db: Session = Depends(get_db)):
    return get_reservations(db)

@router.get("/{reservation_id}", response_model=ReservationRead)
def read_reservation(reservation_id: UUID, db: Session = Depends(get_db)):
    reservation = get_reservation(db, reservation_id)
    if not reservation:
        raise HTTPException(status_code=404, detail="Réservation non trouvée")
    return reservation

@router.post("/", response_model=ReservationRead, status_code=201)
def create_new_reservation(reservation: ReservationCreate, db: Session = Depends(get_db)):
    created = create_reservation(db, reservation)
    if not created:
        raise HTTPException(status_code=400, detail="Salle déjà réservée pour ce créneau")
    return created 