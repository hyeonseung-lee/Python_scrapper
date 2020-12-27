from functions_Indeed import get_jobs as get_indeed_jobs
from functions_SOF import get_jobs as get_sof_jobs
from function_save import save_to_file

indeed_jobs = get_indeed_jobs()
sof_jobs = get_sof_jobs()

jobs = indeed_jobs + sof_jobs
