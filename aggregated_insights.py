import json

# Load the data from the JSON files
with open("fitness_insights.json", "r") as f:
    fitness_data = json.load(f)

with open("sleep_insights.json", "r") as f:
    sleep_data = json.load(f)

with open("journaling_insights.json", "r") as f:
    journaling_data = json.load(f)


# Function to aggregate insights
def aggregate_insights(fitness_data, sleep_data, journaling_data):
    recommendations = []

    # Correlate fitness and sleep data
    for sleep_entry in sleep_data:
        if sleep_entry["sleep_hours"] < 7 and fitness_data[0]["steps"] < 10000:
            recommendations.append(
                "Your sleep hours are below 7, and your daily steps are low. Aim for 10,000 steps and better sleep.")

    # Correlate journaling sentiment and sleep data
    for journal_entry in journaling_data["entries"]:
        if journal_entry["sentiment"] == "negative" and sleep_data[0]["sleep_hours"] < 7:
            recommendations.append(
                "Your journal entries reflect stress, and you are not getting enough sleep. Focus on reducing stress and improving your sleep quality.")

    # Add individual agent recommendations
    for fitness_entry in fitness_data:
        recommendations.append(f"Fitness suggestion for {fitness_entry['date']}: {fitness_entry['suggestion']}")

    for sleep_entry in sleep_data:
        recommendations.append(f"Sleep suggestion for {sleep_entry['date']}: {sleep_entry['suggestion']}")

    # Create combined insights report
    aggregated_report = {
        "recommendations": recommendations
    }

    return aggregated_report


# Generate the aggregated insights
aggregated_insights = aggregate_insights(fitness_data, sleep_data, journaling_data)

# Save the aggregated insights to a file
with open("aggregated_insights.json", "w") as f:
    json.dump(aggregated_insights, f, indent=4)

print("Aggregated insights saved to aggregated_insights.json")
