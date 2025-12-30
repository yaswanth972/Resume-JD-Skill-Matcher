# src/matcher.py
"""Resume to Job Description matching engine using sentence embeddings."""
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from src.preprocess import clean_text

# Load model once for efficiency
model = SentenceTransformer("all-MiniLM-L6-v2")

def match_resume_jd(resume_text: str, jd_text: str) -> float:
    """
    Calculate matching score between resume and job description using cosine similarity
    of sentence embeddings.
    
    Args:
        resume_text: Resume content as string
        jd_text: Job description content as string
        
    Returns:
        Match percentage (0-100)
        
    Raises:
        TypeError: If inputs are not strings
    """
    if not isinstance(resume_text, str) or not isinstance(jd_text, str):
        raise TypeError("Both resume_text and jd_text must be strings")
    
    resume_text = clean_text(resume_text)
    jd_text = clean_text(jd_text)

    embeddings = model.encode([resume_text, jd_text])

    similarity_score = cosine_similarity(
        [embeddings[0]], [embeddings[1]]
    )[0][0]

    match_percentage = round(similarity_score * 100, 2)

    return match_percentage