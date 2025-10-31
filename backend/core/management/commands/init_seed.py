import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from core.models import Company, LeadSource, Lead


class Command(BaseCommand):
    help = "Inicializa superusuario y datos demo (Company, LeadSource, Leads)"

    def handle(self, *args, **options):
        User = get_user_model()
        su_username = os.getenv("DJANGO_SUPERUSER_USERNAME", "admin")
        su_email = os.getenv("DJANGO_SUPERUSER_EMAIL", "admin@example.com")
        su_password = os.getenv("DJANGO_SUPERUSER_PASSWORD", "admin123")

        user, created = User.objects.get_or_create(username=su_username, defaults={
            "email": su_email,
            "is_staff": True,
            "is_superuser": True,
        })
        if created:
            user.set_password(su_password)
            user.save()
            self.stdout.write(self.style.SUCCESS(f"Superusuario creado: {su_username}"))
        else:
            self.stdout.write(self.style.WARNING("Superusuario ya existe"))

        company, _ = Company.objects.get_or_create(name="DemoCorp", defaults={"domain": "democorp.local"})
        source, _ = LeadSource.objects.get_or_create(name="Demo Seed", defaults={"source_type": "seed"})

        leads_data = [
            {"first_name": "Ana", "last_name": "Pérez", "email": "ana@example.com", "phone": "+34123456789"},
            {"first_name": "Luis", "last_name": "García", "email": "luis@example.com", "phone": "+34987654321"},
            {"first_name": "Marta", "last_name": "López", "email": "marta@example.com"},
        ]
        created_count = 0
        for ld in leads_data:
            lead, created_lead = Lead.objects.get_or_create(email=ld.get("email"), defaults={
                "company": company,
                "source": source,
                "first_name": ld.get("first_name"),
                "last_name": ld.get("last_name"),
                "phone": ld.get("phone"),
            })
            if created_lead:
                created_count += 1

        self.stdout.write(self.style.SUCCESS(f"Seed completado. Nuevos leads: {created_count}"))