from rest_framework import serializers

from .models import Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        field = "__all__"
        read_only_fields = ["id", "created_at", "updated_at"]
