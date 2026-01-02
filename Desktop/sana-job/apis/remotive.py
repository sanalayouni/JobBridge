import requests

def fetch_jobs():
    url = "https://remotive.com/api/remote-jobs"

    response = requests.get(url)
    data = response.json()

    jobs = []

    for job in data.get("jobs", []):
        jobs.append({
            "title": job.get("title", ""),
            "description": job.get("description", ""),
            "location": job.get("candidate_required_location", ""),
            "skills": job.get("tags", []),  
            "url": job.get("url", ""),
            "source": "remotive"
        })

    return jobs
