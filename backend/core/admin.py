from django.contrib import admin
from .models import Company, LeadSource, Lead, Interaction, AutomationRule, AutomationLog, Task


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name", "domain", "created_at")


@admin.register(LeadSource)
class LeadSourceAdmin(admin.ModelAdmin):
    list_display = ("name", "source_type", "created_at")


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ("email", "phone", "score", "status_ia", "created_at")
    search_fields = ("email", "phone")


@admin.register(Interaction)
class InteractionAdmin(admin.ModelAdmin):
    list_display = ("lead", "channel", "direction", "timestamp")
    list_filter = ("channel", "direction")


@admin.register(AutomationRule)
class AutomationRuleAdmin(admin.ModelAdmin):
    list_display = ("name", "enabled", "created_at")
    list_filter = ("enabled",)


@admin.register(AutomationLog)
class AutomationLogAdmin(admin.ModelAdmin):
    list_display = ("lead", "action_name", "status", "created_at")
    list_filter = ("status",)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "lead", "status", "due_date", "created_at")
    list_filter = ("status",)