from fastapi import APIRouter
import httpx
from models import Pilot

router = APIRouter()

@router.get("/api/pilot/{pilot_id}", response_model=Pilot)
async def get_pilot(pilot_id: int):
    pilot_url = f"https://swapi.py4e.com/api/people/{pilot_id}/"
    async with httpx.AsyncClient() as client:
        response = await client.get(pilot_url)
        pilot_data = response.json()

        # Assuming species, vehicles and homeworld are included in the pilot data
        return Pilot(
            name=pilot_data["name"],
            height=pilot_data["height"],
            gender=pilot_data["gender"],
            mass=pilot_data["mass"],
            birth_year=pilot_data["birth_year"],
            species_name=pilot_data["species"][0] if pilot_data["species"] else "Unknown",
            vehicles=pilot_data["vehicles"],
            homeworld=pilot_data["homeworld"]
        )