from google.adk.agents import Agent
from google.adk.tools import google_search
from datetime import datetime
import yfinance as yf

def get_curr_time() -> dict:
    return {
        'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'timezone': datetime.now().astimezone().tzname(),
    }

def get_stock_info(symbol: str) -> dict:
    """Get basic stock information - price, company name, and daily change"""
    try:
        stock = yf.Ticker(symbol.upper())
        info = stock.info
        
        return {
            "symbol": symbol.upper(),
            "company": info.get('longName', 'Unknown'),
            "price": info.get('currentPrice', 'N/A'),
            "change": info.get('regularMarketChangePercent', 'N/A')
        }
    except:
        return {"error": f"Couldn't find stock data for {symbol}"}

root_agent = Agent(
    model='gemini-2.0-flash-001',
    name='root_agent',
    description='A helpful assistant that can answer user questions about stock prices and stock market.',
    instruction='Answer user questions about stock prices and stock market. Use the tools provided to get the information you need. Make sure to use the tools correctly. Make sure information is up to date and backed by data. Only answer questions about stock prices and stock market. If users try to ask you anything else, politely decline to answer. You are qualified to give advice on stock market related questions however make sure to add a disclaimer that you are not a financial advisor and that you are not giving financial advice. You are also qualified to make stock market predictions based on the information provided. You are also qualified to make stock market related jokes if the user asks for them.',
    tools=[
        google_search
        #get_stock_info,
        #get_curr_time
    ],
)
