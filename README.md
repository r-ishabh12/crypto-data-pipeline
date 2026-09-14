# Crypto Data Pipeline

An end-to-end data pipeline that extracts live cryptocurrency market data from a public API, cleans and transforms it with Pandas, loads it into a database, and surfaces insights through SQL queries and visualizations.

This project is being built incrementally across multiple versions, each adding a layer of real-world data engineering practice — starting from a simple local script and progressing toward a containerized, orchestrated, cloud-based pipeline.

## Status: Version 0 (complete)

**What it does:**
- Extracts live market data (price, market cap, 24h change) for the top 10 cryptocurrencies via the CoinGecko public API
- Extracts 30 days of historical price data for Bitcoin
- Cleans and transforms the data using Pandas (handling nulls, type casting)
- Loads the cleaned data into a SQLite database
- Runs SQL queries to identify top gainers and average market metrics
- Visualizes the 30-day price trend with Matplotlib

**Tech stack:** Python, Pandas, SQLite, SQL, Matplotlib, Requests

## Roadmap

- **Version 1:** Move from SQLite to PostgreSQL (running in Docker), rewrite the pipeline as a production-style script
- **Version 2:** Add orchestration with Apache Airflow (scheduled runs, retries, failure alerting) and data quality checks
- **Version 3:** Move to a cloud data stack — AWS S3 for raw storage, a data warehouse (Snowflake), dbt for transformation, and a BI dashboard

## Project Structure

crypto-data-pipeline/
├── version0_pipeline.py # Extract, transform, load, query, visualize
├── requirements.txt # Python dependencies
├── .gitignore
└── README.md


## How to Run

```bash
# Clone the repo
git clone https://github.com/yourusername/crypto-data-pipeline.git
cd crypto-data-pipeline

# Set up a virtual environment
python -m venv venv
venv\Scripts\activate      # Windows
# source venv/bin/activate   # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Run the pipeline
python version0_pipeline.py
```

## Example Output

Top gaining coins in the last 24 hours, pulled live and queried via SQL:

| name | current_price | price_change_percentage_24h |
|---|---|---|
| ... | ... | ... |

*(Paste a real sample of your output here once you have it — it makes the README feel alive rather than templated.)*

## Data Source

[CoinGecko API](https://www.coingecko.com/en/api) — free, public, no authentication required.