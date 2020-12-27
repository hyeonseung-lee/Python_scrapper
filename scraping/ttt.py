import os
import requests
from bs4 import BeautifulSoup


URL = f"https://transferwise.com/gb/currency-converter/krw-to-cop-rate?amount=100"
result = requests.get(URL)
soup = BeautifulSoup(result.text, "html.parser")
converted_money = soup.find("input", id="cc-amount-to")
print(converted_money)
