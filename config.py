# config.py

import os

class Config:
    # Configuración común para todos los entornos
    SECRET_KEY = os.getenv('SECRET_KEY', 'mi_clave_secreta')  # Clave secreta para la app
    DEBUG = os.getenv('FLASK_DEBUG', True)  # Habilitar el modo de depuración
    TESTING = os.getenv('FLASK_TESTING', False)  # Para pruebas
    BASE_URL = "https://swapi.py4e.com/api/starships/"  # URL base de la API de Star Wars

class DevelopmentConfig(Config):
    # Configuración para desarrollo
    FLASK_ENV = 'development'

class TestingConfig(Config):
    # Configuración para pruebas
    FLASK_ENV = 'testing'
    TESTING = True
    DATABASE_URI = 'sqlite:///:memory:'  # Usar base de datos en memoria para pruebas

class ProductionConfig(Config):
    # Configuración para producción
    FLASK_ENV = 'production'
    DEBUG = False
