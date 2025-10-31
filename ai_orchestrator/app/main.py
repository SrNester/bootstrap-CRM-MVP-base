from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="AI Orchestrator", version="0.1.0")


class Lead(BaseModel):
    email: str | None = None
    phone: str | None = None
    score_hint: float | None = None


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/ai/score")
def ai_score(lead: Lead):
    base = 0.5
    if lead.score_hint is not None:
        base = lead.score_hint
    if lead.email:
        base += 0.1
    if lead.phone:
        base += 0.1
    score = min(base, 1.0)
    explanation = "Reglas simples basadas en presencia de email/phone y pista de score"
    return {"score": score, "explanation": explanation}