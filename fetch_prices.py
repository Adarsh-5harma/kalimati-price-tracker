import requests
from bs4 import BeautifulSoup
import pandas as pd
session = requests.Session()
response = session.get("https://kalimatimarket.gov.np/price-history")
print("Status:", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

# check what cookies session captured
print(session.cookies.get_dict())

xsrf_token = session.cookies.get("XSRF-TOKEN")

payload = {
    "from": "2020-01-01",
    "to": "2026-08-14",
}

headers = {
    "X-XSRF-TOKEN": xsrf_token,
}

api_response = session.post(
    "https://kalimatimarket.gov.np/api/price-history/105",
    json=payload,
    headers=headers
    )

print("API Status:", api_response.status_code)
print(api_response.text)

data = api_response.json()

df = pd.DataFrame({
    "date": data["prices"]["date"],
    "avg_price": data["prices"]["avg"],
})

df["date"] = pd.to_datetime(df["date"])
df["avg_price"] = df["avg_price"].astype(float)

print(df)
df.to_csv("potato_prices.csv", index=False)
print("Data saved to potato_prices.csv")

print("\nPrice summary:")
print(df["avg_price"].describe())
print("\nHighest price day:")
print(df.loc[df["avg_price"].idxmax()])
print("\nLowest price day:")
print(df.loc[df["avg_price"].idxmin()])