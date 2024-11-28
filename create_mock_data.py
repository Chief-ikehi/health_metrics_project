import json

data = {
    "user_id": "12345",
    "metrics": [
        {"date": "2024-11-22", "steps": 8500, "heart_rate": 75, "sleep_hours": 6.5, "hrv": 45},
        {"date": "2024-11-21", "steps": 9500, "heart_rate": 72, "sleep_hours": 7.2, "hrv": 50}
    ]
}

with open("mock_data.json", "w") as f:
    json.dump(data, f, indent=4)

print("Mock data saved to mock_data.json")
