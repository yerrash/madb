from rest_framework import serializers

from .models import Contact
from companies.serializers import CompanySerializer


class ContactSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)

    class Meta:
        model = Contact
        field = "__all__"
        read_only_fields = ["id"]
