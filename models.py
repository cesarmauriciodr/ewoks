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
