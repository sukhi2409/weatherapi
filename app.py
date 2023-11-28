from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/weather', methods=['GET'])
def get_weather():
    api_key = "562eea4c4937b1baaeeb59a2ac52d2ba"  
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    # Get location from query parameter
    location = request.args.get('location')

    if not location:
        return jsonify({"error": "Location parameter is missing"}), 400

    # Prepare parameters for the API request
    params = {
        'q': location,
        'appid': api_key,
        'units': 'metric'  # You can change units to 'imperial' for Fahrenheit
    }

    # Make the API request
    response = requests.get(base_url, params=params)
    data = response.json()

    # Check if the request was successful
    if response.status_code == 200:
        # Extract relevant information from the API response
        weather_data = {
            'location': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
        }
        return jsonify(weather_data)
    else:
        return jsonify({"error": "Unable to retrieve weather data"}), 500

if __name__ == '__main__':
    app.run(debug=True)
