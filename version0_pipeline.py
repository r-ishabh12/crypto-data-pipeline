import requests
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

url = "https://api.coingecko.com/api/v3/coins/markets"
params = {"vs_currency": "usd", "order": "market_cap_desc", "per_page": 10, "page": 1}

response = requests.get(url, params=params)
data = response.json()   # converts API's JSON response into Python list/dict

print(data[0])   # look at the first coin's data



df = pd.DataFrame(data)          # turn the API response into a table
df.head()                        # see first 5 rows
df.info()                        # see column types, nulls
df.isnull().sum()                # count missing values per column
# df = df.dropna()                 # drop rows with missing values (or df.fillna(0) to fill instead)
# df["price_rupees"] = df["current_price"] * 83   # add a new calculated column
# df_sorted = df.sort_values("price_change_percentage_24h", ascending=False)  # sort

df = df[["id", "name", "current_price", "market_cap", "price_change_percentage_24h", "total_volume"]]
df = df.dropna()
df["current_price"] = df["current_price"].astype(float)
df["price_change_percentage_24h"] = df["price_change_percentage_24h"].round(2)

print(len(df))   # should now print 10
df.head()



conn = sqlite3.connect("crypto.db")   # creates a database file (in Colab's cloud storage)
df.to_sql("coin_prices", conn, if_exists="replace", index=False)   # load your DataFrame into a SQL table

query = """
SELECT name, current_price, price_change_percentage_24h
FROM coin_prices
ORDER BY price_change_percentage_24h DESC
LIMIT 5
"""
top_gainers = pd.read_sql(query, conn)
print(top_gainers)

avg_market_cap = pd.read_sql("SELECT AVG(market_cap) as avg_cap FROM coin_prices", conn)
print(avg_market_cap)

hist_url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
hist_params = {"vs_currency": "usd", "days": 30}
hist_response = requests.get(hist_url, params=hist_params)
hist_data = hist_response.json()

prices = hist_data["prices"]   # list of [timestamp, price]
hist_df = pd.DataFrame(prices, columns=["timestamp", "price"])
hist_df["date"] = pd.to_datetime(hist_df["timestamp"], unit="ms")
hist_df.head()



plt.figure(figsize=(10,5))
plt.plot(hist_df["date"], hist_df["price"])
plt.title("Bitcoin Price — Last 30 Days")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.xticks(rotation=45)
plt.show()