import requests

url = "https://api.coingecko.com/api/v3/coins/markets"
params = {"vs_currency": "usd", "order": "market_cap_desc", "per_page": 10, "page": 1}

response = requests.get(url, params=params)
data = response.json()   # converts API's JSON response into Python list/dict

print(data[0])   # look at the first coin's data

import pandas as pd

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

import sqlite3

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