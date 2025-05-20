# ResearchScope AI - Intelligent Project Analysis System

ResearchScope AI is an advanced project analysis system that leverages multiple AI agents to perform comprehensive research and analysis of technical projects. The system uses Google's Gemini model to power a team of specialized agents that work together to extract insights, gather research, and validate project requirements.

## Features

- Keyword extraction from project descriptions
- Web scraping for research papers
- Automated research summarization
- Project requirement validation
- Sequential processing using CrewAI framework
- Powered by Google's Gemini Pro model

## Example Project Description

Here's an **example** of how to use the system with a technical project:

```python
project_description = """
Project: Smart Home Energy Management System

Develop an AI-powered energy management system for smart homes that can:
1. Monitor and analyze real-time energy consumption patterns
2. Predict energy usage based on historical data and weather conditions
3. Automatically optimize energy distribution across different home systems
4. Provide personalized recommendations for energy savings
5. Integrate with existing smart home devices and solar panel systems

The system should be scalable, secure, and capable of handling multiple data sources while maintaining user privacy.
"""

result = analyze_project(project_description)
```

## Setup

1. Clone this repository
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the project root and add your Google API key:
   ```
   GOOGLE_API_KEY=your_google_api_key_here
   ```

## Usage

1. Import the project analysis function:
   ```python
   from project_analysis_crew import analyze_project
   ```

2. Call the function with your project description:
   ```python
   project_description = """
   Your project description here
   """
   result = analyze_project(project_description)
   print(result)
   ```

## Project Structure

- `project_analysis_crew.py`: Main implementation file containing the agents and their tasks
- `requirements.txt`: Project dependencies
- `.env`: Environment variables (create this file with your API keys)

## Agents

1. **Keyword Extractor**: Analyzes project descriptions and extracts key technical terms
2. **Research Agent**: Searches for and analyzes relevant research papers
3. **Summarization Expert**: Creates comprehensive summaries of research findings
4. **Validation Expert**: Validates alignment between project requirements and research

## Note

The web scraping functionality is implemented using a simplified approach. For production use, consider:
- Using academic APIs (e.g., Semantic Scholar, arXiv)
- Implementing more robust web scraping
- Adding rate limiting and error handling
- Using proper academic paper databases 