from pydantic import BaseModel
"""
This module defines data models using Pydantic's BaseModel for a Star Wars themed application.

Classes:
    Pilot: Represents a pilot with attributes such as name, height, gender, mass, birth year, species name, vehicles, and homeworld.
    ShipGeneral: Represents general information about a ship including name, model, cost in credits, and max atmosphering speed.
    ShipSpecific: Inherits from ShipGeneral and adds specific attributes such as crew and passengers.
    UpdateShip: Represents the data required to update a ship's information including name, model, cost in credits, max atmosphering speed, crew, passengers, and pilots.
"""
from typing import List


# Modelos de datos
class Pilot(BaseModel):
    """
    Represents a pilot with attributes such as name, height

    Attributes:
        name (str): The name of the pilot.
        height (str): The height of
        gender (str): gender
        mass (str): mass
        birth_year (str): birth year
        species_name (str): species name
        vehicles (List[str]): vehicles
        homeworld (str): homeworld
    """
    name: str
    height: str
    gender: str
    mass: str
    birth_year: str
    species_name: str
    vehicles: List[str]
    homeworld: str


class ShipGeneral(BaseModel):
    """
    Represents general information about a ship.

    Attributes:
        name (str): The name of the ship.
        model (str): The model of the ship.
        cost_in_credits (str): The cost of the ship in credits.
        max_atmosphering_speed (str): The maximum atmosphering speed of the ship.
    """
    name: str
    model: str
    cost_in_credits: str
    max_atmosphering_speed: str


class ShipSpecific(ShipGeneral):
    """
    Represents specific information about a ship.

    Attributes:
        name (str): The name of the ship.
        model (str): The model of the ship.
        cost_in_credits (str): The cost of the ship in credits.
        max_atmosphering_speed (str): The maximum atmosphering speed of the ship.

        crew (str): The number of crew members on the ship.
        passengers (str): The number of passengers the ship can carry.
    """
    crew: str
    passengers: str


class UpdateShip(BaseModel):
    """
    Represents the data required to update a ship's information.

    Attributes:
        name (str): The updated name of the ship.
        model (str): The updated model of the ship.
        cost_in_credits (str): The updated cost of the ship in credits.
        max_atmosphering_speed (str): The updated maximum atmosphering speed of the ship.
        crew (str): The updated number of crew members on the ship.
        passengers (str): The updated number of passengers the ship can carry.
        pilots (List[str]): The updated list of pilots associated with the ship.
    """

    name: str
    model: str
    cost_in_credits: str
    max_atmosphering_speed: str
    crew: str
    passengers: str
    pilots: List[str]
