from sqlalchemy import Column, String, Date, Time, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid
from app.database.database import Base

class Reservation(Base):
    __tablename__ = "reservations"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    salle_id = Column(UUID(as_uuid=True), ForeignKey("salles.id"), nullable=False)
    date = Column(Date, nullable=False)
    heure = Column(Time, nullable=False)
    utilisateur = Column(String, nullable=False)
    commentaire = Column(String, nullable=True) 