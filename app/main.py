from fastapi import FastAPI

from app.routers import salle, reservation

app = FastAPI(
    title="API de réservation de salles",
    description="API REST pour la gestion des réservations de salles (FastAPI, SQLAlchemy, SQLite)",
    version="1.0.0",
)

app.include_router(salle.router)
app.include_router(reservation.router)

@app.get("/")
async def root():
    return {"message": "Bienvenue sur l'API de réservation de salles !"}