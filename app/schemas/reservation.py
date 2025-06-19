from pydantic import BaseModel, UUID4
from typing import Optional
from datetime import date, time

class ReservationBase(BaseModel):
    salle_id: UUID4
    date: date
    heure: time
    utilisateur: str

class ReservationCreate(ReservationBase):
    pass

class ReservationRead(ReservationBase):
    id: UUID4
    class Config:
        orm_mode = True 