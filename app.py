from flask import Flask, request, jsonify

app = Flask(__name__)

# Global variable to store the latest readings
latest_sensor_data = {"pm25": 0, "pm10": 0}

@app.route('/update', methods=['POST'])
def update():
    global latest_sensor_data
    data = request.json
    if data:
        latest_sensor_data = data
        return "OK", 200
    return "Invalid data", 400

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(latest_sensor_data), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
