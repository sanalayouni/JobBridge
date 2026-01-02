# AI Job–Candidate Matching System

## 📌 Project Overview

This project is an **AI-powered job–candidate matching system** that uses **semantic embeddings (deep learning)** to intelligently match a candidate profile with job offers.

Instead of relying on keyword-based matching (e.g. TF-IDF), this system understands the **meaning** of skills, job titles, and descriptions using **Sentence Transformers**.

The system is designed following **real-world, production-ready principles**, including:

* Legal and ethical data sourcing
* Scalable architecture
* Modular design

---

## 🎯 Motivation

Traditional job matching systems fail because:

* They rely on exact keyword overlap
* They cannot understand synonyms or context
* They rank irrelevant jobs too highly

This project solves these problems by:

* Using **AI embeddings** to capture semantic meaning
* Comparing candidate and job vectors using **cosine similarity**
* Ranking jobs by relevance

---

## 🧠 Model Used

### Sentence Transformers

* Model: `all-MiniLM-L6-v2`
* Type: **Deep Learning Transformer model**
* Architecture: Based on **BERT**
* Output: Dense semantic vectors (384 dimensions)

This model allows the system to understand that:

* *"Backend Developer" ≈ "Python Engineer"*
* *"REST APIs" ≈ "Web services"*

---

## 📂 Project Structure

```
project/
│
├── data/
│   ├── candidate.json
│   ├── jobs_raw.json
│   ├── jobs_processed.json
│
├── scraper/
│   └── adzuna_fetch.py
│
├── matcher/
│   └── match_jobs.py
│
├── requirements.txt
├── README.md
```

---

## 📥 Data Sources

### ✅ Adzuna API (Official)

This project **does not scrape LinkedIn or similar platforms**.

Instead, it uses **Adzuna**, an official job-market API, because:

* Scraping LinkedIn violates Terms of Service
* APIs provide structured, legal, and reliable data
* This reflects real-world industry practices

> ⚠️ Data access is a **legal and architectural decision**, not just a technical one.

---

## 🧾 Candidate Data Format (`candidate.json`)

```json
{
  "job_title": "Python Backend Developer",
  "skills": ["Python", "Django", "REST APIs", "SQL", "Docker"],
  "location": "Tunisia"
}
```

---

## 🧾 Job Data Format (`jobs_processed.json`)

```json
{
  "title": "Backend Developer (Python)",
  "company": "Tech Company",
  "location": "Tunis",
  "description": "Looking for a Python backend developer..."
}
```

---

## ⚙️ Installation

### 1️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Verify Installation

```bash
python -c "from sentence_transformers import SentenceTransformer; print('OK')"
```

---

## 🚀 How It Works

### Step 1: Fetch Jobs

Jobs are fetched from Adzuna API and saved locally as JSON.

### Step 2: Build Text Representations

Candidate and job data are converted into natural-language text blocks.

### Step 3: Generate Embeddings

Using `SentenceTransformer`, texts are converted into dense vectors.

### Step 4: Similarity Scoring

Cosine similarity is used to compute match scores between candidate and jobs.

### Step 5: Ranking

Jobs are ranked from most relevant to least relevant.

---

## 📊 Example Output

```
Backend Developer (Python) → 68.3%
Python Developer → 67.5%
Senior Backend Engineer → 64.1%
```

---

## ❓ Why Not Scrape LinkedIn?

Scraping LinkedIn:

* Violates Terms of Service
* Can lead to legal consequences
* Is unstable and easily blocked
* Is not production-ready

Using official APIs ensures:

* Compliance
* Data quality
* Scalability

---

## 🛠 Technologies Used

* Python
* Sentence Transformers
* Scikit-learn
* Adzuna API
* JSON

---
## 🔮 Future Improvements

* Multi-candidate support
* Skill weighting
* Experience level matching
* Hybrid scoring (AI + rules)
* Web dashboard

---

## 🏁 Conclusion

This project demonstrates how **AI embeddings** can be used to build a smart, ethical, and scalable job-matching system aligned with industry best practices.

---

## 👤 Author

**Sana Layouni**

---

## 📄 License

This project is for educational and research purposes.
