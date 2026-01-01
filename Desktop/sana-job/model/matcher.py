from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load model once
model = SentenceTransformer("all-MiniLM-L6-v2")

def build_candidate_text(candidate):
    return f"""
    Job title: {candidate['job_title']}
    Skills: {' '.join(candidate['skills'])}
    Skills: {' '.join(candidate['skills'])}
    Location: {candidate['location']}
    """

def build_job_text(job):
    return f"""
    Job title: {job.get('title', '')}
    Description: {job.get('description', '')}
    Skills: {' '.join(job.get('skills', []))}
    Location: {job.get('location', '')}
    """

def match_candidate(candidate, jobs):
    candidate_text = build_candidate_text(candidate)
    job_texts = [build_job_text(job) for job in jobs]

    candidate_embedding = model.encode(candidate_text)
    job_embeddings = model.encode(job_texts)

    scores = cosine_similarity(
        candidate_embedding.reshape(1, -1),
        job_embeddings
    )[0]

    for i, job in enumerate(jobs):
        job["match_score"] = round(float(scores[i]) * 100, 2)

    return sorted(jobs, key=lambda x: x["match_score"], reverse=True)
