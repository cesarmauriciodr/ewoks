from fastapi import APIRouter
import httpx
from models import ShipGeneral, ShipSpecific, UpdateShip
from typing import List


router = APIRouter()



from pydantic import BaseModel
from typing import List

# Modelos de datos
class Pilot(BaseModel):
    name: str
    height: str
    gender: str
    mass: str
    birth_year: str
    species_name: str
    vehicles: List[str]
    homeworld: str

class ShipGeneral(BaseModel):
    name: str
    model: str
    cost_in_credits: str
    max_atmosphering_speed: str

class ShipSpecific(ShipGeneral):
    crew: str
    passengers: str

class UpdateShip(BaseModel):
    name: str
    model: str
    cost_in_credits: str
    max_atmosphering_speed: str
    crew: str
    passengers: str
    pilots: List[str]


BASE_URL = "https://swapi.py4e.com/api/starships/"

@router.get("/api/starships_general", response_model=List[ShipGeneral])
async def get_all_ships():
    async with httpx.AsyncClient() as client:
        response = await client.get(BASE_URL)
        data = response.json()
        ships = data.get("results", [])
        return [
            ShipGeneral(
                name=ship["name"],
                model=ship["model"],
                cost_in_credits=ship["cost_in_credits"],
                max_atmosphering_speed=ship["max_atmosphering_speed"],
            )
            for ship in ships
        ]

@router.get("/api/starships_specific", response_model=ShipSpecific)
async def get_ship(ship_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}{ship_id}/")
        ship = response.json()
        return ShipSpecific(
            name=ship["name"],
            model=ship["model"],
            cost_in_credits=ship["cost_in_credits"],
            max_atmosphering_speed=ship["max_atmosphering_speed"],
            crew=ship["crew"],
            passengers=ship["passengers"]
        )
    




@router.put("/api/starships_update", response_model=UpdateShip)
async def update_ship(ship_id: int, update_ship: UpdateShip):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}{ship_id}/")
        ship = response.json()
        update_data = update_ship.dict()
        update_data.pop("pilots", None)
        ship.update(update_data)
        response = await client.put(f"{BASE_URL}{ship_id}/", json=ship)
        return update_ship
    
