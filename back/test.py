from flask_api import FlaskAPI
from flask_cors import CORS, cross_origin
import json

app = FlaskAPI(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/about.json')
@cross_origin()
def about():
    with open('about.json') as file:
        about = json.load(file)
        print(about)
    return about

@app.route('/widgets')
@cross_origin()
def widgets():
    widgets = [
        {
            "id": 1,
            "name": "city_temperature",
            "description": "Display temperature for a city",
            "params":
            {
                "name": "Montpellier"
            }
        },
        {
            "id": 2,
            "name": "city_temperature",
            "description": "Display temperature for a city",
            "params":
            {
                "name": "Paris"
            }
        }
    ]
    return widgets

if __name__ == "__main__":
    app.run(debug=True)
