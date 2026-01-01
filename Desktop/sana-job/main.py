import json
from model.matcher import match_candidate

with open("data/candidate.json") as f:
    candidate = json.load(f)

with open("data/jobs.json") as f:
    jobs = json.load(f)

ranked_jobs = match_candidate(candidate, jobs)

print("\n🔹 Top Job Matches:\n")
for job in ranked_jobs:
    print(f"{job['title']} → {job['match_score']}%")
