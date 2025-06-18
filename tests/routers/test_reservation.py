import pytest
from fastapi.testclient import TestClient
from app.main import app
from datetime import date, time

client = TestClient(app)

def test_create_and_list_reservation():
    # Créer une salle d'abord
    salle_resp = client.post("/salles/", json={
        "nom": "Salle Test",
        "capacite": 10,
        "localisation": "Bâtiment X"
    })
    salle_id = salle_resp.json()["id"]
    # Créer une réservation
    reservation_data = {
        "salle_id": salle_id,
        "date": str(date.today()),
        "heure": "10:00:00",
        "utilisateur": "user1"
    }
    resp = client.post("/reservations/", json=reservation_data)
    assert resp.status_code == 201
    # Tenter de réserver le même créneau
    resp2 = client.post("/reservations/", json=reservation_data)
    assert resp2.status_code == 400
    # Lister les réservations
    resp3 = client.get("/reservations/")
    assert resp3.status_code == 200
    assert isinstance(resp3.json(), list) 