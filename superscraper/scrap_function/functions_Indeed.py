import requests
from bs4 import BeautifulSoup

LIMIT = 50


def extract_pages(URL):
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, 'html.parser')

    # pagination
    pagination = soup.find("div", {"class": "pagination"})
    if pagination:
        links = pagination.find_all("a")
    else:
        return 0
    spans = []

    for link in links[:-1]:
        spans.append(int(link.string))

    max_page = spans[-1]
    return max_page


def extract_job(html, URL):
    # get title
    title = html.find("h2", {"class": "title"}).find("a")["title"]

    # get company
    company = html.find("span", {"class": "company"})
    company_anchor = company.find("a")

    if company_anchor is not None:
        company = str(company_anchor.string)
    else:
        company = str(company.string)
    company = company.strip()

    # get location
    location = html.find("div", {"class": "recJobLoc"})["data-rc-loc"]

    # get id to
    job_id = html["data-jk"]

    return {"title": title,
            "company": company,
            "location": location,
            "link": URL + f"&vjk={job_id}"}


def extract_jobs(last_page, URL):
    jobs = []

    for page in range(last_page):
        result = requests.get(f"{URL}&start={LIMIT*page}")
        soup = BeautifulSoup(result.text, 'html.parser')
        results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})

        for result in results:
            job = extract_job(result, URL)
            jobs.append(job)

        print(f"indeed page {page + 1} done.")
    return jobs


def get_jobs(word):
    URL = f"https://kr.indeed.com/jobs?q={word}&l=%EC%84%9C%EC%9A%B8&limit={LIMIT}&radius=25"
    last_page = extract_pages(URL)
    jobs = extract_jobs(last_page, URL)

    return jobs
