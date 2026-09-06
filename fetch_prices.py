import requests
from bs4 import BeautifulSoup

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

