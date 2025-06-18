from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.dialects.postgresql import UUID
import uuid
from app.database.database import Base

class Salle(Base):
    __tablename__ = "salles"
    id = Column(String(36), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    nom = Column(String, nullable=False)
    capacite = Column(Integer, nullable=False)
    localisation = Column(String, nullable=False)
    disponible = Column(Boolean, default=True) 