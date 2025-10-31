import os
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Lead
from .tasks import score_lead


@receiver(post_save, sender=Lead)
def lead_created_score(sender, instance: Lead, created: bool, **kwargs):
    if created:
        if os.getenv("DISABLE_LEAD_SIGNALS", "False") in ("True", "true", "1"):
            return
        try:
            score_lead.delay(instance.id)
        except Exception:
            # Evita romper operaciones si el broker no está disponible
            pass