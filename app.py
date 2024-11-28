from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/health_data', methods=['GET'])
def get_health_data():
    with open("normalized_data.json", "r") as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
