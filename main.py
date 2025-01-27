from fastapi import FastAPI
from endpoints import ships, pilots

app = FastAPI()

# Incluir routers
app.include_router(ships.router)
app.include_router(pilots.router)