from sqlalchemy.orm import Session
from app.models.reservation import Reservation
from app import models
from app.schemas.reservation import ReservationCreate
from uuid import UUID
from typing import List, Optional
from datetime import date, time

def get_reservations(db: Session) -> List[Reservation]:
    return db.query(Reservation).all()

def get_reservation(db: Session, reservation_id: UUID) -> Optional[Reservation]:
    return db.query(Reservation).filter(Reservation.id == str(reservation_id)).first()

def get_reservations_by_salle_date_heure(db: Session, salle_id: str, date_: date, heure_: time) -> List[Reservation]:
    return db.query(Reservation).filter(
        Reservation.salle_id == str(salle_id),
        Reservation.date == date_,
        Reservation.heure == heure_
    ).all()

def create_reservation(db: Session, reservation: ReservationCreate) -> Optional[Reservation]:
    # Vérifier la disponibilité
    existing = get_reservations_by_salle_date_heure(db, str(reservation.salle_id), reservation.date, reservation.heure)
    if existing:
        return None
    reservation_dict = reservation.dict()
    reservation_dict["salle_id"] = str(reservation_dict["salle_id"])
    db_reservation = Reservation(**reservation_dict)
    db.add(db_reservation)
    db.commit()
    db.refresh(db_reservation)
    return db_reservation 

def delete_reservation(db: Session, reservation_id: UUID) -> None:
    res = db.get(models.Reservation, reservation_id)
    if res is None:
        raise HTTPException(status_code=404, detail="Reservation not found")
    db.delete(res)
    db.commit()