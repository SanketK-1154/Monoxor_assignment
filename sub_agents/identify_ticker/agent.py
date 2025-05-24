import os
import requests
from dotenv import load_dotenv
from google.adk.agents import Agent

load_dotenv()


def get_identify_ticker(company_name: str) -> str:
    api_key = os.environ.get("ALPHA_VANTAGE_API_KEY")
    if not api_key:
        return "UNKNOWN_TICKER"

    url = 'https://www.alphavantage.co/query'
    params = {
        "function": "SYMBOL_SEARCH",
        "keywords": company_name,
        "apikey": api_key
    }
    try:
        res = requests.get(url, params=params)
        matches = res.json().get("bestMatches", [])
        if matches:
            return matches[0].get("1. symbol", "UNKNOWN_TICKER")
        return "UNKNOWN_TICKER"
    except Exception as e:
        print(f"Error: {e}")
        return "UNKNOWN_TICKER"


identify_ticker = Agent(
    model='gemini-2.0-flash-001',
    name='identify_ticker',
    description=''' Ticker Identify Agent
    ''',
    instruction='''
    You must extract the correct stock **ticker symbol** from the user's query.

 After giving the answer delegate back to the root_agent.
 ''',
    tools=[get_identify_ticker],
)
