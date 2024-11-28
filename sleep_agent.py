import json

with open("normalized_data.json", "r") as f:
    data = json.load(f)

def analyze_sleep(data):
    insights = []
    for metric in data["metrics"]:
        sleep_hours = metric["sleep_hours"]
        if sleep_hours < 7:
            suggestion = "Consider a consistent bedtime routine to improve sleep quality."
        else:
            suggestion = "You're getting enough sleep. Keep up the good habits!"
        insights.append({
            "date": metric["date"],
            "sleep_hours": sleep_hours,
            "suggestion": suggestion
        })
    return insights

sleep_insights = analyze_sleep(data)

with open("sleep_insights.json", "w") as f:
    json.dump(sleep_insights, f, indent=4)

print("Sleep insights saved to sleep_insights.json")
