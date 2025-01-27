from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_all_ships():
    response = client.get("/api/nave_general")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_pilot():
    response = client.get("/api/pilotos/") 
    assert response.status_code == 200
    assert "name" in response.json()

def test_get_specific_ship():
    response = client.get("/api/nave_especifica?ship_id=9")
    assert response.status_code == 200
    assert "name" in response.json()

def test_update_ship():
    response = client.put("/api/actualizar_nave", json={"name": "updated_name"})
    assert response.status_code == 200
    assert response.json()["name"] == "updated_name"