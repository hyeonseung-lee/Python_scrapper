import os
import csv
import requests
from bs4 import BeautifulSoup

os.system("clear")
URL = "http://www.alba.co.kr"


def get_companys():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    companys = soup.find_all("ul", {"class": "goodsBox"})
    companys = companys[1].find_all(
        "a", {"class": "goodsBox-info"})

    return companys


def extract_company(html):
    title = html.find_all("span", {"class": "company"})
    link = html["href"]
    return {"title": title,
            "link": link}


def extracting_company():
    companys = []
    for company in get_companys():
        companys.append(extract_company(company))
    return companys


def get_last_page(link):
    link = f"{link}/job/brand"
    print(link)
    result = requests.get(link)
    soup = BeautifulSoup(result.text, "html.parser")
    divs = soup.find("div", {"id": "NormalInfo"})
    print(divs)


results = []


def extract_jobs(link):
    global results
    result = requests.get(link)
    soup = BeautifulSoup(result.text, "html.parser")
    table = soup.find("tbody")
    jobs = table.find_all("tr")
    for job in jobs:
        location = job.find("td", {"class": "local"})
        if location:
            location = location.get_text()
            title = job.find("td", {"class": "title"})
            title = title.find("span", {"class": "company"}).get_text()
            if title:
                date = job.find("td", {"class": "data"}).get_text()
                if date:
                    pay = job.find("td", {"class": "pay"})
                    tp = pay.find("span", {"class": "payIcon"}).get_text()
                    pays = pay.find("span", {"class": "number"}).get_text()

                    if pays:
                        up = job.find("td", {"class": "last"}).get_text()

                        if up:
                            results.append({"place": location,
                                            "title": title,
                                            "time": date,
                                            "pay": tp + pays,
                                            "date": up})
                    else:
                        continue
                else:
                    continue
            else:
                continue
        else:
            continue

    return results


def save_to_file(jobs):
    file = open("jobs.csv", mode="w")

    writer = csv.writer(file)
    writer.writerow(["place", "title", "time", "pay", "date"])

    for job in jobs:
        writer.writerow(list(job.values()))
    file.close()
    return


companys = extracting_company()
for company in companys:
    extract_jobs(company["link"])

save_to_file(results)
