from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_all_ships():
    response = client.get("/api/starships_general")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_pilot():
    response = client.get("/api/pilot/1") 
    assert response.status_code == 200
    assert "name" in response.json()

def test_get_specific_ship():
    response = client.get("/api/starships_specific?ship_id=9")
    assert response.status_code == 200
    assert "name" in response.json()
    

def test_update_ship():
    json = {
        "name": "Death Star",
        "model": "DS-1 Orbital Battle Station",
        "cost_in_credits": "1000000000000",
        "max_atmosphering_speed": "n/a",
        "crew": "342,953",
        "passengers": "843,342",
    }
    response = client.put("/api/starships_update?ship_id=9", json=json)
    assert response.status_code == 422

