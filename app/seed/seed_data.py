from app.database.database import SessionLocal
from app.models.salle import Salle
from app.models.reservation import Reservation
from datetime import date, time
import uuid

def seed():
    db = SessionLocal()
    try:
        # Nettoyage de la base
        db.query(Reservation).delete()
        db.query(Salle).delete()
        db.commit()

        # === SALLES ===
        salles = [
            Salle(id=str(uuid.uuid4()), nom="Salle A", capacite=20, localisation="Bâtiment 1", disponible=True),
            Salle(id=str(uuid.uuid4()), nom="Salle B", capacite=10, localisation="Bâtiment 2", disponible=True),
        ]
        db.add_all(salles)
        db.commit()

        # === RESERVATIONS ===
        reservations = [
            Reservation(
                id=str(uuid.uuid4()),
                salle_id=salles[0].id,
                date=date.today(),
                heure=time(10, 0),
                utilisateur="alice",
            ),
            Reservation(
                id=str(uuid.uuid4()),
                salle_id=salles[1].id,
                date=date.today(),
                heure=time(11, 0),
                utilisateur="bob",
            ),
        ]
        db.add_all(reservations)
        db.commit()
        print("Seed terminé !")
    finally:
        db.close()

if __name__ == "__main__":
    seed()