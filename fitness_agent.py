import json

with open("normalized_data.json", "r") as f:
    data = json.load(f)

def analyze_activity(data):
    insights = []
    for metric in data["metrics"]:
        steps = metric["steps"]
        if steps < 10000:
            suggestion = "Try to increase your daily steps to at least 10,000 for improved health."
        else:
            suggestion = "Great job staying active! Maintain this level of activity."
        insights.append({
            "date": metric["date"],
            "steps": steps,
            "suggestion": suggestion
        })
    return insights

activity_insights = analyze_activity(data)

with open("fitness_insights.json", "w") as f:
    json.dump(activity_insights, f, indent=4)

print("Fitness insights saved to fitness_insights.json")
