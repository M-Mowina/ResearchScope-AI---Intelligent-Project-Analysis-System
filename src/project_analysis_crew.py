from crewai import Agent, Task, Crew, Process
from langchain.tools import Tool
from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables
load_dotenv()

api_key = os.getenv('GOOGLE_API_KEY')

print(f"Your API key is: {api_key}")
# Configure the LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-pro",
    temperature=0.7,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

class WebScraperTool:
    def scrape_web(self, query):
        """
        Scrape web for research papers based on the query
        """
        # This is a simplified version. In a real implementation, you'd want to use
        # academic APIs or more sophisticated web scraping
        search_url = f"https://scholar.google.com/scholar?q={query}"
        try:
            response = requests.get(search_url)
            soup = BeautifulSoup(response.text, 'html.parser')
            results = []
            
            # Extract paper titles and snippets
            for result in soup.find_all('div', class_='gs_ri')[:5]:  # Get top 5 results
                title = result.find('h3')
                snippet = result.find('div', class_='gs_rs')
                if title and snippet:
                    results.append({
                        'title': title.text,
                        'snippet': snippet.text
                    })
            return results
        except Exception as e:
            return f"Error scraping web: {str(e)}"

# Create tools
web_scraper = WebScraperTool()
scraper_tool = Tool(
    name="WebScraper",
    func=web_scraper.scrape_web,
    description="Scrapes the web for research papers based on keywords"
)

# Create agents
keyword_extractor = Agent(
    role='Keyword Extractor',
    goal='Extract key technical terms and concepts from project descriptions',
    backstory="""You are an expert at analyzing technical project descriptions 
    and extracting the most relevant keywords and concepts.""",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

researcher = Agent(
    role='Research Agent',
    goal='Find and analyze relevant research papers based on keywords',
    backstory="""You are an expert researcher who can find and analyze 
    relevant academic papers and technical documentation.""",
    tools=[scraper_tool],
    verbose=True,
    allow_delegation=False,
    llm=llm
)

summarizer = Agent(
    role='Summarization Expert',
    goal='Create comprehensive summaries of research findings',
    backstory="""You are an expert at condensing complex technical information 
    into clear, concise summaries while maintaining accuracy.""",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

validator = Agent(
    role='Validation Expert',
    goal='Validate and compare project requirements with research findings',
    backstory="""You are an expert at validating technical requirements and 
    ensuring alignment between project goals and research findings.""",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

def analyze_project(project_description):
    # Create tasks
    keyword_task = Task(
        description=f"""Analyze the following project description and extract key technical terms 
        and concepts that would be relevant for research:
        
        {project_description}""",
        agent=keyword_extractor
    )

    research_task = Task(
        description="""Using the extracted keywords, search for and analyze relevant research papers 
        and technical documentation. Focus on finding papers that address the key concepts.""",
        agent=researcher
    )

    summary_task = Task(
        description="""Create a comprehensive summary of the research findings, focusing on how they 
        relate to the project requirements. Highlight key insights and potential applications.""",
        agent=summarizer
    )

    validation_task = Task(
        description="""Compare the original project description with the research summary. 
        Validate if the research findings align with the project requirements and identify any gaps 
        or areas that need additional research.""",
        agent=validator
    )

    # Create crew
    crew = Crew(
        agents=[keyword_extractor, researcher, summarizer, validator],
        tasks=[keyword_task, research_task, summary_task, validation_task],
        verbose=2,
        process=Process.sequential
    )

    # Execute the crew's tasks
    result = crew.kickoff()
    return result

if __name__ == "__main__":
    # Example usage
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
    print("\nFinal Analysis Result:")
    print(result) 