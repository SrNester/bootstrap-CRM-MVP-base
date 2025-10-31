import os
import requests
from celery import shared_task
from .models import Lead


@shared_task
def score_lead(lead_id: int):
    try:
        lead = Lead.objects.get(id=lead_id)
    except Lead.DoesNotExist:
        return {"status": "not_found", "lead_id": lead_id}

    ai_url = os.getenv("AI_SERVICE_URL", "http://ai:9000")
    try:
        resp = requests.post(f"{ai_url}/ai/score", json={
            "email": lead.email,
            "phone": lead.phone,
        }, timeout=10)
        data = resp.json()
        lead.score = float(data.get("score", 0.0))
        lead.ai_explanation = data.get("explanation", "")
        lead.save(update_fields=["score", "ai_explanation"])
        return {"status": "updated", "score": lead.score}
    except Exception as e:
        return {"status": "error", "error": str(e)}