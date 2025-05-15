# Stock Analysis Based on News Sentiment and Price Trends

This Python script performs a simple stock analysis by combining **news sentiment** with **recent price trends** for a given Brazilian stock ticker.

## How It Works

1. The user enters a stock ticker (e.g., `PETR4`, `AERI3`).
2. The script fetches recent news articles using the [NewsAPI](https://newsapi.org).
3. Sentiment analysis is performed using the `nltk` VADER tool.
4. Historical stock price data (last 30 days) is retrieved using `yfinance`.
5. A recommendation is generated: **Buy**, **Sell**, or **Hold**.

## Recommendation Logic

- **Buy**: News sentiment is positive and the current price is below the 30-day average.
- **Sell**: News sentiment is negative and the current price is above the 30-day average.
- **Hold**: All other cases.

-- Setup

Install the required packages with:

```bash
pip install -r requirements.txt

## Setup and Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/stock-news-analysis.git
   cd stock-news-analysis
Install the dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Get your API key from NewsAPI.

Open the script file and replace the placeholder:

python
Copy
Edit
api_key = 'YOUR_API_KEY_HERE'
Run the script:

bash
Copy
Edit
python analise_acoes.py
Dependencies
pandas

requests

yfinance

nltk

To install manually:

bash
Copy
Edit
pip install pandas requests yfinance nltk
Notes
NewsAPI has a request limit on the free tier.

Stock price data from yfinance may not be 100% accurate or up to date.

This tool is for educational and experimental use.

csharp
Copy
Edit

