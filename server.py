from flask import Flask, jsonify, send_file
import math


app = Flask(__name__)


# Planet data (simplified): distance from Sun (AU), orbital period (days), relative radius (km -> for display scaling), color
PLANETS = [
{"name": "Mercury", "distance_au": 0.387, "period_days": 88, "radius_km": 2440, "color": "#b2a08f"},
{"name": "Venus", "distance_au": 0.723, "period_days": 224.7, "radius_km": 6052, "color": "#f0d7a0"},
{"name": "Earth", "distance_au": 1.000, "period_days": 365.25, "radius_km": 6371, "color": "#4a90e2"},
{"name": "Mars", "distance_au": 1.524, "period_days": 687, "radius_km": 3390, "color": "#d14b3f"},
{"name": "Jupiter", "distance_au": 5.204, "period_days": 4331, "radius_km": 69911, "color": "#d4a36a"},
{"name": "Saturn", "distance_au": 9.582, "period_days": 10747, "radius_km": 58232, "color": "#e6c98b"},
{"name": "Uranus", "distance_au": 19.20, "period_days": 30589, "radius_km": 25362, "color": "#8fd7e6"},
{"name": "Neptune", "distance_au": 30.05, "period_days": 59800, "radius_km": 24622, "color": "#3b6bd6"}
]


@app.route('/')
def index():
    return send_file('index.html')


@app.route('/api/planets')
def planets():
  return jsonify({"planets": PLANETS})


if __name__ == '__main__':
    app.run(debug=True)