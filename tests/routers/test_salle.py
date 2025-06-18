import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_salle():
    response = client.post("/salles/", json={
        "nom": "Salle A",
        "capacite": 20,
        "localisation": "Bâtiment 1"
    })
    assert response.status_code == 201
    data = response.json()
    assert data["nom"] == "Salle A"
    assert data["capacite"] == 20
    assert data["localisation"] == "Bâtiment 1"
    assert "id" in data

def test_list_salles():
    response = client.get("/salles/")
    assert response.status_code == 200
    assert isinstance(response.json(), list) 