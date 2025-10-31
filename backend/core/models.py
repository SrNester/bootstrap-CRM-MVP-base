from django.conf import settings
from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=200)
    domain = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class LeadSource(models.Model):
    name = models.CharField(max_length=100)
    source_type = models.CharField(max_length=50, default="manual")  # manual, csv, form, api
    metadata = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.source_type})"


class Lead(models.Model):
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, blank=True, null=True)
    source = models.ForeignKey(LeadSource, on_delete=models.SET_NULL, blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    score = models.FloatField(default=0.0)
    ai_explanation = models.TextField(blank=True, null=True)
    status_ia = models.CharField(max_length=50, blank=True, null=True)  # interesado, requiere_demo, etc.
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email or self.phone or f"Lead {self.pk}"


class Interaction(models.Model):
    CHANNEL_CHOICES = (
        ("email", "Email"),
        ("whatsapp", "WhatsApp"),
    )
    DIRECTION_CHOICES = (
        ("outbound", "Outbound"),
        ("inbound", "Inbound"),
    )
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE, related_name="interactions")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)
    channel = models.CharField(max_length=20, choices=CHANNEL_CHOICES)
    direction = models.CharField(max_length=20, choices=DIRECTION_CHOICES, default="outbound")
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.channel} {self.direction} -> Lead {self.lead_id}"


class AutomationRule(models.Model):
    name = models.CharField(max_length=200)
    condition = models.JSONField()  # e.g. {"lead.score": ">", "value": 0.8}
    action = models.JSONField()     # e.g. {"type": "assign_user", "user_id": 1}
    enabled = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class AutomationLog(models.Model):
    rule = models.ForeignKey(AutomationRule, on_delete=models.SET_NULL, blank=True, null=True)
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE)
    action_name = models.CharField(max_length=100)
    status = models.CharField(max_length=50, default="executed")
    details = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Task(models.Model):
    STATUS_CHOICES = (
        ("pending", "Pendiente"),
        ("in_progress", "En progreso"),
        ("done", "Completada"),
    )
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE, related_name="tasks")
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    due_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title