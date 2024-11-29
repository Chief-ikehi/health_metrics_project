# AI-Powered Wearable Insights Dashboard
## Introduction
This project is an AI-powered system that processes and analyzes data from wearables to provide actionable insights. It features fitness tracking, sleep analysis, and journaling sentiment analysis agents, combined in a modular, scalable architecture. Users can view recommendations and aggregated insights through a dashboard or API output.

## Features
**Fitness Tracking Agent**: Provides workout suggestions based on activity data.  
**Sleep Analysis Agent**: Analyzes sleep patterns and provides improvement tips.  
**Journaling Sentiment Analysis Agent**: Detects emotional tone and offers feedback.  
**Insights Aggregation Layer**: Combines outputs from all agents to generate holistic recommendations.  
**Dashboard**: Displays user metrics and insights.  

## Setup Instructions

1. Clone the repository:
       ```
       git clone https://github.com/Chief-ikehi/health_metrics_project.git
       ```  
2. Navigate to the project directory:
       ```
       cd health_metrics_project
       ```  
3. Install dependencies:
       ```
       pip install -r requirements.txt
       ```  
4. Run the dashboard (optional):  
       ```
       cd dashboard_project
       ```  
       ```
       python app.py
       ```  
6. View JSON outputs (optional):
Aggregated insights and agent outputs can be found in the folder.
    
# AI Agents
- **Fitness Tracking Agent:** Analyzes activity data to provide workout suggestions using a rule-based system and thresholds (e.g., steps, active minutes).
- **Sleep Analysis Agent:** Uses time-series data to detect poor sleep patterns and offer advice.
- **Journaling Sentiment Analysis Agent:** Uses the VADER sentiment analyzer to classify emotions (positive, negative, neutral) and offer emotional feedback.
    
# Insights Aggregation
The aggregation layer combines outputs from individual agents to provide holistic recommendations. For example, it correlates poor sleep with negative emotions or low activity.

# Dashboard
The dashboard is a web-based interface built with Flask, allowing users to view their metrics, insights, and recommendations in a user-friendly format.

# Challenges Faced
- **Sentiment Analysis Precision:** Switching from TextBlob to VADER ensured more accurate classification of journal entries.
- **Mock Data:** The system was designed to handle both mock datasets and wearable APIs, ensuring flexibility during testing.
- **Scalability:** Designed a modular structure to allow easy integration of additional AI agents or data sources.
