from scrap_function.functions_Indeed import get_jobs as get_indeed_jobs
from scrap_function.functions_SOF import get_jobs as get_sof_jobs


def integrated_get_jobs(word):
    indeed_jobs = get_indeed_jobs(word)
    sof_jobs = get_sof_jobs(word)

    jobs = indeed_jobs + sof_jobs

    return jobs
