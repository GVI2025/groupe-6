from sqlalchemy.orm import Session
from app.models.salle import Salle
from app.schemas.salle import SalleCreate, SalleUpdate
from uuid import UUID
from typing import List, Optional

def get_salles(db: Session) -> List[Salle]:
    return db.query(Salle).all()

def get_salle(db: Session, salle_id: UUID) -> Optional[Salle]:
    return db.query(Salle).filter(Salle.id == salle_id).first()

def create_salle(db: Session, salle: SalleCreate) -> Salle:
    db_salle = Salle(**salle.dict())
    db.add(db_salle)
    db.commit()
    db.refresh(db_salle)
    return db_salle

def update_salle(db: Session, salle_id: UUID, salle: SalleUpdate) -> Optional[Salle]:
    db_salle = get_salle(db, salle_id)
    if not db_salle:
        return None
    for key, value in salle.dict(exclude_unset=True).items():
        setattr(db_salle, key, value)
    db.commit()
    db.refresh(db_salle)
    return db_salle

def delete_salle(db: Session, salle_id: UUID) -> bool:
    db_salle = get_salle(db, salle_id)
    if not db_salle:
        return False
    db.delete(db_salle)
    db.commit()
    return True 