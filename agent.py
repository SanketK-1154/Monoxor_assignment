from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
from numpy.ma.core import identity

from Stock_Market_Guru.sub_agents.identify_ticker.agent import identify_ticker
from Stock_Market_Guru.sub_agents.ticker_analysis.agent import ticker_analysis
from Stock_Market_Guru.sub_agents.ticker_news.agent import ticker_news
from Stock_Market_Guru.sub_agents.ticker_price.agent import ticker_price
from Stock_Market_Guru.sub_agents.ticker_price_change.agent import ticker_price_change

root_agent = Agent(
    model='gemini-2.0-flash-001',
    name='root_agent',
    description=''' Stocks Agent
    ''',
    instruction='''You are the main controller of a modular stock query system.

This system consists of 5 modular sub-agents:

 identify_ticker – Parses the user query and identifies the corresponding stock ticker (e.g., "Tesla" → "TSLA").

 ticker_news– Retrieves the most recent and relevant news articles about the identified stock (uses Google Search or other APIs).

 ticker_price – Fetches the current price of the stock, including historical open and close prices.

 ticker_price_change – Calculates how the stock’s price has changed over various timeframes (7 days, 1 month, 3 months, 6 months, and 1 year).

 ticker_analysis – Analyzes and summarizes the reason behind recent price movements using the combined output of `ticker_news`, `ticker_price`, and `ticker_price_change`.

 You are responsible for delegating tasks to the following agent:
    - identify_ticker
    - ticker_price
    - ticker_price_change
    
    
    You also have access to the following tools:
    - ticker_news
    - ticker_analysis
    
Your responsibility is to orchestrate all these sub-agents depending on the user’s query type.
''',
    sub_agents=[identify_ticker, ticker_price, ticker_price_change],
     tools=[
         AgentTool(ticker_news),
         AgentTool(ticker_analysis)
     ],
)
