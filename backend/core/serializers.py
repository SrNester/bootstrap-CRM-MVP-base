from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Lead, Company, LeadSource


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "is_active"]


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ["id", "name", "domain", "created_at"]


class LeadSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeadSource
        fields = ["id", "name", "source_type", "metadata", "created_at"]


class LeadSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)
    source = LeadSourceSerializer(read_only=True)
    company_id = serializers.IntegerField(write_only=True, required=False, allow_null=True)
    source_id = serializers.IntegerField(write_only=True, required=False, allow_null=True)
    
    class Meta:
        model = Lead
        fields = [
            "id",
            "company",
            "source", 
            "company_id",
            "source_id",
            "first_name",
            "last_name",
            "email",
            "phone",
            "score",
            "ai_explanation",
            "status_ia",
            "created_at",
        ]