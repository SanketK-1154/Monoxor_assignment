# 📈 Stock Market Multi-Agent System

A modular AI-powered assistant built using **Google ADK**, capable of answering stock-related queries such as:
- Current price
- Historical changes
- News headlines
- Price movement analysis

This system uses **multiple collaborating agents** and integrates with the **Alpha Vantage API** and **Google Search**.

---

## 🚀 Features

- ✅ Multi-agent orchestration using Google ADK
- 🔍 Company name to stock ticker resolution
- 📊 Real-time and historical stock price via Alpha Vantage
- 📰 Live news headlines via Google Search
- 🧠 Smart reasoning and analysis using LLM

---

## 🧰 Tech Stack

- Python
- Google Agent Development Kit (ADK)
- Alpha Vantage API (Free tier)
- `google_search` tool for news
- `dotenv` for API key management

---

## ⚙️ Setup Instructions

 1. Clone the Repo

git clone https://github.com/your-username/stock-market-guru.git
cd stock-market-guru

2. Install Requirements
   
   pip install google-adk

4. Get Alpha Vantage API Key

    Register at https://www.alphavantage.co/support/#api-key

    Add it to a .env file:

ALPHA_VANTAGE_API_KEY=your_api_key_here

4. Run the App

You can run it as a command-line ADK agent or integrate into a web app.
