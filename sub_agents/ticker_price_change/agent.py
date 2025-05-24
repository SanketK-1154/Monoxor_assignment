import os
import requests
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

def get_price_change(ticker: str) -> dict:
    print(f"--- Tool: get_price_change called for {ticker} ---")

    api_key = os.environ.get("ALPHA_VANTAGE_API_KEY")
    if not api_key:
        return {
            "status": "error",
            "error_message": "Missing Alpha Vantage API key."
        }

    url = 'https://www.alphavantage.co/query'
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": ticker,
        "outputsize": "full",  # Full 20+ year history
        "apikey": api_key
    }

    try:
        response = requests.get(url, params=params)
        data = response.json().get("Time Series (Daily)", {})
        if not data:
            return {"status": "error", "error_message": "No historical data available."}

        # Convert to {date: close_price}
        parsed_data = {datetime.strptime(date, "%Y-%m-%d"): float(prices["4. close"])
                       for date, prices in data.items()}
        sorted_dates = sorted(parsed_data.keys(), reverse=True)
        today = sorted_dates[0]
        today_price = parsed_data[today]

        # Define timeframes (approximate days)
        timeframes = {
            "7_days": 7,
            "1_month": 30,
            "3_months": 90,
            "6_months": 180,
            "1_year": 365,
        }

        results = {}
        for label, days_ago in timeframes.items():
            past_date = today - timedelta(days=days_ago)
            # Find the nearest date before past_date
            available_past_dates = [d for d in sorted_dates if d <= past_date]
            if not available_past_dates:
                results[label] = "No data"
                continue
            closest_past = available_past_dates[0]
            past_price = parsed_data[closest_past]

            abs_change = round(today_price - past_price, 2)
            pct_change = round((abs_change / past_price) * 100, 2)

            results[label] = {
                "old_price": round(past_price, 2),
                "current_price": round(today_price, 2),
                "abs_change": abs_change,
                "pct_change": pct_change,
                "past_date": closest_past.strftime("%Y-%m-%d"),
                "current_date": today.strftime("%Y-%m-%d")
            }

        return {
            "status": "success",
            "ticker": ticker,
            "timeframe_changes": results,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

    except Exception as e:
        return {
            "status": "error",
            "error_message": f"Error fetching data: {str(e)}"
        }


from google.adk.agents import Agent

ticker_price_change = Agent(
    name="ticker_price_change",
    model="gemini-2.0-flash-001",
    description=""" Stock Price change Agent
""",
    instruction="""
You are responsible for calculating percentage and absolute price changes over the following timeframes:
- Last 7 days
- Last 1 month
- Last 3 months
- Last 6 months
- Last 1 year

Follow these instructions:

1. Use the `get_price_change` tool with the provided ticker.

2. For each timeframe, calculate:
   - Old Price
   - Current Price
   - Absolute Price Change
   - Percentage Price Change

3. Format the output like this:

4. Round all price values to 2 decimal places and percent changes to 2 decimal places.

5. If data is missing for a timeframe, skip it or mention “No data”.

6. Do **not** provide any reasons or analysis for the price movements — only show the changes.

You are a data retrieval agent focused purely on historical price comparison.

After giving the answer delegate back to the root_agent.
""",
    tools=[get_price_change],
)
