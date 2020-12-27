import requests
from bs4 import BeautifulSoup

words = "python"
URL = f"https://stackoverflow.com/jobs?q={words}"


def get_last_page():
    print(URL)
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pages = soup.find("div", {"class": "s-pagination"}).find_all("a")
    last_page = pages[-2].get_text(strip=True)

    return int(last_page)


def extract_job(html):
    # get_title
    title = html.find("a", {"class": "s-link"})['title']

    # get_company & location
    company, location = html.find(
        "h3", {"class": "mb4"}
    ).find_all(
        "span", recursive=False)

    company, location = company.get_text(
        strip=True), location.get_text(strip=True)

    # get jobid
    job_id = html['data-jobid']

    return {"title": title,
            "company": company,
            "location": location,
            "apply_link": f"https://stackoverflow.com/jobs/{job_id}/"}


def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        result = requests.get(f"{URL}&pg={page+1}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "-job"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
            print(job)
        print(f"sof page {page + 1} done.")

    return jobs


def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs
