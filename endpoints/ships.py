"""
This module defines API endpoints for interacting with starships using FastAPI.

Endpoints:
- GET /api/starships_general: Retrieve a list of general information about all starships.
- GET /api/starships_specific: Retrieve specific information about a starship by its ID.
- PUT /api/starships_update: Update information about a starship by its ID.

"""

from fastapi import APIRouter
import httpx
from models import ShipGeneral, ShipSpecific, UpdateShip
from typing import List


router = APIRouter()


BASE_URL = "https://swapi.py4e.com/api/starships/"


@router.get("/api/starships_general", response_model=List[ShipGeneral])
async def get_all_ships():
    """
    Endpoint to retrieve all starships.

    This endpoint fetches data from an external API and returns a list of starships
    with general information.

    Returns:
        List[ShipGeneral]: A list of starships with general information.
    """
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
    """
    Endpoint to retrieve specific information about a starship.

    This endpoint fetches data from an external API and returns specific information
    about a starship based on the provided ID.

    Args:
        ship_id (int): The ID of the starship to retrieve.

    Returns:
        ShipSpecific: A model containing specific information about the starship.

    """
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}{ship_id}/")
        ship = response.json()
        return ShipSpecific(
            name=ship["name"],
            model=ship["model"],
            cost_in_credits=ship["cost_in_credits"],
            max_atmosphering_speed=ship["max_atmosphering_speed"],
            crew=ship["crew"],
            passengers=ship["passengers"],
        )


@router.put("/api/starships_update", response_model=UpdateShip)
async def update_ship(ship_id: int, update_ship: UpdateShip):
    """
    Endpoint to update information about a starship.

    This endpoint fetches the current information about a starship from an external API,
    updates the information based on the provided data, and then sends the updated data back
    to the external API.

    Args:
        ship_id (int): The ID of the starship to update.

    Returns:
        UpdateShip: The updated information for the starship.

    """

    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}{ship_id}/")
        ship = response.json()
        update_data = update_ship.dict()
        update_data.pop("pilots", None)
        ship.update(update_data)
        response = await client.put(f"{BASE_URL}{ship_id}/", json=ship)
        return update_ship
