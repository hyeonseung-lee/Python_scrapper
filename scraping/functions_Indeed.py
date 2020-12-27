import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://kr.indeed.com/jobs?q=python&l=%EC%84%9C%EC%9A%B8&limit={LIMIT}&radius=25"


def extract_pages():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, 'html.parser')

    # pagination
    pagination = soup.find("div", {"class": "pagination"})
    print(pagination)
    links = pagination.find_all("a")
    spans = []

    for link in links[:-1]:
        spans.append(int(link.string))

    max_page = spans[-1]
    print(max_page)
    return max_page


def extract_job(html):
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
            "link": f"https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=python&l=%EC%84%9C%EC%9A%B8&limit=50&radius=25&start=0&vjk={job_id}"}


def extract_jobs(last_page):
    jobs = []

    for page in range(last_page):
        result = requests.get(f"{URL}&start={LIMIT*page}")
        soup = BeautifulSoup(result.text, 'html.parser')
        results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})

        for result in results:
            job = extract_job(result)
            jobs.append(job)

        print(f"indeed page {page + 1} done.")
    return jobs


def get_jobs():
    last_page = extract_pages()
    jobs = extract_jobs(last_page)

    return jobs
