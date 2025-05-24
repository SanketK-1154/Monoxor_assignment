import os
import requests
from dotenv import load_dotenv

load_dotenv()

def get_current_stock_price(ticker: str) -> dict:
    api_key = os.environ.get("ALPHA_VANTAGE_API_KEY")
    if not api_key:
        return {"status": "error", "message": "Missing API key."}

    url = 'https://www.alphavantage.co/query'
    params = {
        "function": "GLOBAL_QUOTE",
        "symbol": ticker,
        "apikey": api_key
    }

    try:
        response = requests.get(url, params=params)
        data = response.json().get("Global Quote", {})

        if not data:
            return {"status": "error", "message": f"No data for {ticker}"}

        return {
            "status": "success",
            "ticker": ticker.upper(),
            "price": float(data.get("05. price", 0.0)),
            "change": float(data.get("09. change", 0.0)),
            "percent_change": data.get("10. change percent", "0%"),
        }

    except Exception as e:
        return {"status": "error", "message": str(e)}
from google.adk.agents import Agent

ticker_price = Agent(
    name="ticker_price",
    model="gemini-2.0-flash-001",
    description=""" Stock Price Agent
""",
    instruction="""
Given a valid stock ticker symbol (like "TSLA") or company name, use the get_current_stock_price tool to fetch the latest stock price data.

Your output must include:
- Current price
- Absolute change
- Percentage change

Format your response like this:
Stock Price for [TICKER]

Price: $XXX.XX
Change: $±YY.YY
Change Percent: ±ZZ.ZZ%

If the ticker is invalid or data is unavailable, respond with:
"Price data not available for [TICKER]"
After giving the answer delegate back to the root_agent.
""",
    tools=[get_current_stock_price],
)
