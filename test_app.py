import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_nave_general(client):
    rv = client.get('/api/nave_general')
    assert rv.status_code == 200
    data = rv.get_json()
    assert len(data) > 0

def test_piloto(client):
    rv = client.get('/api/piloto')
    assert rv.status_code == 200
    data = rv.get_json()
    assert len(data) > 0

def test_nave_especifica(client):
    rv = client.get('/api/nave_especifica')
    assert rv.status_code == 200
    data = rv.get_json()
    assert "name" in data

def test_actualizar_nave(client):
    data = {
        "name": "Millennium Falcon",
        "model": "YT-1300 Corellian light freighter",
        "cost_in_credits": "100000",
        "max_atmosphering_speed": "1050",
        "cargo_capacity": "100000",
        "passengers": "6",
        "pilots": ["Han Solo", "Chewbacca"]
    }
    rv = client.post('/api/actualizar_nave', json=data)
    assert rv.status_code == 200
    updated_data = rv.get_json()
    assert updated_data["name"] == "Millennium Falcon"
