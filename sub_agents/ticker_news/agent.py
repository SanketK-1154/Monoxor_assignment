from google.adk.agents import Agent
from google.adk.tools import google_search

ticker_news = Agent(
    name="ticker_news",
    model="gemini-2.0-flash-001",
    description="""
News Agent
""",
    instruction="""
   
  You are a helpful assistant that can analyze news articles and provide a summary of the news.
    When asked about news, you should use the google_search tool to search for the news about the company or the ticker and give the
    related news or the article as an output.
    
    After giving the answer delegate back to the root_agent.
""",
 tools=[google_search],
)
