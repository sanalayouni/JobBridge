from apis.adzuna import fetch_jobs
from apis.remotive import fetch_jobs as fetch_remotive_jobs
def fetch_all_jobs():
    jobs = []
    jobs.extend(fetch_jobs())
    jobs.extend(fetch_remotive_jobs())
    return jobs
