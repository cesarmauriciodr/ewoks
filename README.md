# ewoks -- Starship Inventory API

Este proyecto consiste en una API que permite obtener información sobre las naves y pilotos del Imperio Galáctico.

## Endpoints

### /api/starships_general
- Devuelve una lista de todas las naves con su nombre, modelo, costo y velocidad máxima.

### /api/pilot
- Devuelve una lista de los pilotos, su nombre, altura, género, peso, año de nacimiento, especie, vehículos que han piloteado y su planeta de origen.

### /api/starships_specific
- Devuelve los detalles de una nave específica, incluyendo capacidad de carga y pasajeros.

### /api/starships_update
- Permite actualizar los detalles de una nave, incluyendo los pilotos asignados.

## Requisitos
- Python 3.x
- FastApi
- pydantic
- pytest

## Instalación

```bash
pip install -r requirements.txt

```

## Ejecución

```bash 
python app.py
```

## testing

```bash

pytest

```


¡Que la fuerza lo acompañe!
