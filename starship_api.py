import requests
from flask import current_app

def get_starships():
    response = requests.get(current_app.config['BASE_URL'])
    data = response.json()
    starships = []
    for starship in data['results']:
        starships.append({
            "name": starship["name"],
            "model": starship["model"],
            "cost_in_credits": starship["cost_in_credits"],
            "max_atmosphering_speed": starship["max_atmosphering_speed"]
        })
    return starships
