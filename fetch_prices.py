import requests
from bs4 import BeautifulSoup

session = requests.Session()
response = session.get("https://kalimatimarket.gov.np/price-history")
print("Status:", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

# check what cookies session captured
print(session.cookies.get_dict())