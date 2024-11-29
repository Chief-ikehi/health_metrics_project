from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

# Load aggregated insights from JSON file
with open("aggregated_insights.json", "r") as f:
    aggregated_data = json.load(f)

@app.route("/")
def dashboard():
    # Pass aggregated data to the HTML template
    return render_template("dashboard.html", data=aggregated_data)

if __name__ == "__main__":
    app.run(debug=True)
