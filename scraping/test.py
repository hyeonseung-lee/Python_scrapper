import os
import requests
from bs4 import BeautifulSoup

os.system("clear")
url = "https://www.iban.com/currency-codes"

result = requests.get(url)
soup = BeautifulSoup(result.text, "html.parser")
tds = soup.find("tbody").find_all("tr")

countries = []
for td in tds:
    country = [components.string for components in td.find_all("td")]
    if country[1] == "No universal currency":
        continue
    else:
        countries.append(country)


def search_country_and_currency():
    global countries
    while True:
        try:
            search_number = int(input("#: "))
            if 0 <= search_number < len(countries):
                country = countries[search_number]
                print(country[0] + "\n")
                print(country)
                return country[2]
            else:
                print("Choose a number from the list")
                continue
        except ValueError:
            print("That wasn't a number.")


def convert_currency():
    print("Where are you from? Choose a country by number. \n")
    from_code = search_country_and_currency()
    print("\nNow choose another country.")
    another_code = search_country_and_currency()
    print(f"\nHow many {from_code} do you want to convert to {another_code}")
    while True:

        try:
            mount = int(input())
            URL = f"https://transferwise.com/gb/currency-converter/{from_code}-to-{another_code}-rate?amount={mount}"
            result = requests.get(URL)
            soup = BeautifulSoup(result.text, "html.parser")
            converted_money = soup.find("input")
            if converted_money:
                converted_money = float(converted_money["value"])
                converted_money *= mount
                print(f"{from_code} {mount} is {another_code} {converted_money}")
                return converted_money
            else:
                print(
                    f"There are no currency information {from_code} to {another_code}")
                return

        except ValueError:
            print("That wasn't a number.")


# printing countries
print("Welcome to CurrencyConvert PRO 2000 \n")
for i in range(len(countries)):
    print(f"# {i} {countries[i][0]}")
print("\n")

convert_currency()
