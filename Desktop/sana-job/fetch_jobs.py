import requests
import json

APP_ID = "e83c7d66"
APP_KEY = "ea5b0762a880de0066c8e784c32b88f5"

url = "https://api.adzuna.com/v1/api/jobs/fr/search/1"

params = {
    "app_id": APP_ID,
    "app_key": APP_KEY,
    "results_per_page": 20,
    "what": "software developer",
    "where": "France",
    "content-type": "application/json"
}

response = requests.get(url, params=params)
data = response.json()

jobs = []

for job in data.get("results", []):
    jobs.append({
        "title": job["title"],
        "company": job.get("company", {}).get("display_name", ""),
        "description": job.get("description", ""),
        "location": job.get("location", {}).get("display_name", ""),
        "url": job.get("redirect_url", "")
    })

with open("data/jobs.json", "w", encoding="utf-8") as f:
    json.dump(jobs, f, ensure_ascii=False, indent=2)

print("Jobs saved to data/jobs.json")
