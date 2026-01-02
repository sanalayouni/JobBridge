import json
import os
from aggregator import fetch_all_jobs
from model.matcher import match_candidate

# Ensure data folder exists
os.makedirs("data", exist_ok=True)

# Fetch jobs
jobs = fetch_all_jobs()

# Save jobs
with open("data/jobs.json", "w", encoding="utf-8") as f:
    json.dump(jobs, f, ensure_ascii=False, indent=2)

# Load candidate
with open("data/candidate.json", encoding="utf-8") as f:
    candidate = json.load(f)

# Match candidate with jobs
ranked_jobs = match_candidate(candidate, jobs)

# Show results
print("\n🔹 Top Job Matches:\n")
for job in ranked_jobs[:10]:
    print(f"{job['title']} → {job['match_score']}%")
