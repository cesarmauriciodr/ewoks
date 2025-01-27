from flask import Flask, jsonify
from starship_api import get_starships, get_pilot_info, get_specific_starship, update_starship
from config import DevelopmentConfig  # Importar configuración de desarrollo

# Crear la aplicación Flask y cargar la configuración
app = Flask(__name__)
app.config.from_object(DevelopmentConfig)  # Usar la configuración de desarrollo

@app.route('/api/nave_general', methods=['GET'])
def nave_general():
    starships = get_starships()
    return jsonify(starships), 200

@app.route('/api/piloto', methods=['GET'])
def piloto():
    pilots = get_pilot_info()
    return jsonify(pilots), 200

@app.route('/api/nave_especifica', methods=['GET'])
def nave_especifica():
    starship_name = 'Millennium Falcon'  # Nombre de la nave por defecto, o puede ser dinámico
    starship_details = get_specific_starship(starship_name)
    return jsonify(starship_details), 200

@app.route('/api/actualizar_nave', methods=['POST'])
def actualizar_nave():
    data = request.get_json()
    updated_starship = update_starship(data)
    return jsonify(updated_starship), 200

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])
