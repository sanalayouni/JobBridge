import requests

APP_ID = "e83c7d66"
APP_KEY = "ea5b0762a880de0066c8e784c32b88f5"

def fetch_jobs():
    url = "https://api.adzuna.com/v1/api/jobs/fr/search/1"

    params = {
        "app_id": APP_ID,
        "app_key": APP_KEY,
        "results_per_page": 20,
        "what": "software developer",
        "where": "France",
    }

    response = requests.get(url, params=params)
    data = response.json()

    jobs = []
    for job in data.get("results", []):
        jobs.append({
            "title": job.get("title", ""),
            "company": job.get("company", {}).get("display_name", ""),
            "description": job.get("description", ""),
            "location": job.get("location", {}).get("display_name", ""),
            "skills": [],
            "url": job.get("redirect_url", ""),
            "source": "adzuna"
        })

    return jobs
