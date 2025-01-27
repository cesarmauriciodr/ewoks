"""
Retrieve pilot information from the Star Wars API.
Endpoints:

- GET /api/pilot/{pilot_id}: Retrieve information about a pilot by their ID.
"""

from fastapi import APIRouter
import httpx
from models import Pilot

router = APIRouter()

BASE_URL = "https://swapi.py4e.com/api/people/"


@router.get("/api/pilot/{pilot_id}", response_model=Pilot)
async def get_pilot(pilot_id: int):
    """
    Endpoint to retrieve pilot information.

    This endpoint fetches data from an external API and returns information
    about a pilot based on the provided ID.

    Args:
        pilot_id (int): The ID of the pilot to retrieve.

    Returns:

        Pilot: A model containing information about the pilot.
    """
    pilot_url = f"{BASE_URL}{pilot_id}/"
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
            species_name=(
                pilot_data["species"][0] if pilot_data["species"] else "Unknown"
            ),
            vehicles=pilot_data["vehicles"],
            homeworld=pilot_data["homeworld"],
        )
