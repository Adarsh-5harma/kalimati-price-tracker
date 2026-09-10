import requests
from bs4 import BeautifulSoup
import pandas as pd


session = requests.Session()
response = session.get("https://kalimatimarket.gov.np/commodity-price-history")
soup = BeautifulSoup(response.content, "html.parser")
print("Status Code:", response.status_code)
xsrf_token = session.cookies.get("XSRF-TOKEN")

vegetables = {
    "Potato white": "105",
    "Tomato Nepali":"101.1",
    "Onion Indian":"106.1",
    "cabbage":"108.1",
    "mushroom":"144.1",
}

for name, commodity_id in vegetables.items():
    print(f"\nFetching data for {name} (ID: {commodity_id})...")

    api_response = session.post(
        f"https://kalimatimarket.gov.np/api/price-history/{commodity_id}",
        data={"from": "2020-01-01", "to": "2026-08-14"},
        headers = {"X-XSRF-TOKEN": xsrf_token,}
    )

    data = api_response.json()
    df = pd.DataFrame({
        "date": data["prices"]["date"],
        "avg_price": data["prices"]["avg"],
    })

    df["date"] = pd.to_datetime(df["date"])
    df["avg_price"] = df["avg_price"].astype(float)


    filename = name.lower().replace( " ", "_") + ".csv"
    df.to_csv(filename, index=False)
    print(f"Saved {len(df)} rows to {filename}")

