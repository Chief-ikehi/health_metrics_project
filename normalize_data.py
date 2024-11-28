import json

with open("mock_data.json", "r") as f:
    data = json.load(f)

for metric in data["metrics"]:
    metric["steps"] = max(0, metric["steps"])  # to prevent negative steps
    metric["heart_rate"] = max(40, metric["heart_rate"]) # minimum heart rate
    metric["sleep_hours"] = max(0, metric["sleep_hours"])  # to prevent negative sleep hours
    metric["hrv"] = max(0, metric["hrv"])  # to prevent negative HRV

with open("normalized_data.json", "w") as f:
    json.dump(data, f, indent=4)

print("Normalized data saved to normalized_data.json")
