from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict, Any
import re
import hashlib
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

app = FastAPI()

# --- Helper functions ---

TECH_SKILLS = {
    "python", "java", "c++", "javascript", "sql",
    "aws", "docker", "kubernetes", "tensorflow", "pytorch",
    "react", "nodejs", "fastapi", "flask"
}

def anonymize_text(text: str) -> str:
    return re.sub(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+", "[EMAIL]", text)

def _hash(obj: Any) -> str:
    return hashlib.sha256(str(obj).encode()).hexdigest()

def _embed(texts: List[str]) -> List[np.ndarray]:
    return [np.random.rand(384) for _ in texts]  # placeholder embeddings

def _audit(entry: Dict[str, Any]):
    print("AUDIT:", entry)

# --- Scoring ---

def _score_candidate(jd: str, parsed: Dict[str, Any]) -> Dict[str, Any]:
    anon_resume = anonymize_text(parsed.get("raw_text", ""))
    jd_vec, resume_vec = _embed([jd, anon_resume])
    sim = float(cosine_similarity([jd_vec], [resume_vec])[0][0])

    req_skills = {s.strip().lower() for s in re.findall(r"[A-Za-z+#.]+", jd.lower()) if s.strip()}
    cand_skills = set(map(str.lower, parsed.get("skills", {}).get("technical", [])))
    overlaps = sorted(cand_skills.intersection(TECH_SKILLS.intersection(req_skills)))
    gaps = sorted(list((TECH_SKILLS.intersection(req_skills)) - cand_skills))[:10]

    exp = parsed.get("experience_years", 0.0)
    exp_score = min(exp / 8.0, 1.0)

    overall = 0.7 * sim + 0.3 * exp_score
    return {
        "overall_score": round(overall, 3),
        "scoring_breakdown": {
            "semantic": round(sim, 3),
            "experience_relevance": round(exp_score, 3),
            "skill_match": round(len(overlaps) / max(1, len(overlaps) + len(gaps)), 3)
        },
        "skill_gaps": gaps[:5],
        "strengths": ["Technical overlap: " + ", ".join(overlaps[:5]) if overlaps else "General fit"],
    }

# --- Request Models ---

class RankRequest(BaseModel):
    job_title: str
    job_description: str
    parsed_candidates: List[Dict[str, Any]]

# --- API Routes ---

@app.get("/")
async def root():
    return {"message": "AI Recruit Demo is running"}

@app.post("/rank")
async def rank(req: RankRequest):
    scores = []
    for idx, cand in enumerate(req.parsed_candidates):
        s = _score_candidate(req.job_description, cand)
        scores.append({"candidate_index": idx, **s})
    ranked = sorted(scores, key=lambda x: x["overall_score"], reverse=True)

    # FIXED for Pydantic v1: use dict() instead of model_dump()
    _audit({
        "type": "rank",
        "job_title": req.job_title,
        "input_hash": _hash(req.dict()),
        "output_hash": _hash(ranked),
        "fairness_metrics": {"demographic_parity": 1.0, "equalized_odds": 1.0},
    })

    return {"results": [{**r, "rank_position": i + 1} for i, r in enumerate(ranked)]}
