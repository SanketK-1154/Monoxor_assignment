from google.adk.agents import Agent
from google.adk.tools import google_search

ticker_analysis = Agent(
    name="ticker_analysis",
    model="gemini-2.0-flash-001",
    description="""Analysis Agent
""",
    instruction="""
    Analyze and summarizes the reason behind recent price movements.
    When asked about analysis you should use the google search tool to search for the daily summary and reason for 
    price movements for the company or ticker and give a formatted summarised answer.
    
    After giving the answer delegate back to the root_agent.
""",
    tools=[google_search],
)
