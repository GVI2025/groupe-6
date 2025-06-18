from pydantic import BaseModel, UUID4
from typing import Optional

class SalleBase(BaseModel):
    nom: str
    capacite: int
    localisation: str
    disponible: Optional[bool] = True

class SalleCreate(SalleBase):
    pass

class SalleUpdate(BaseModel):
    nom: Optional[str]
    capacite: Optional[int]
    localisation: Optional[str]
    disponible: Optional[bool]

class SalleRead(SalleBase):
    id: UUID4
    class Config:
        orm_mode = True 