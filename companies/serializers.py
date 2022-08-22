from rest_framework import serializers

from contacts.models import Contact
from contacts.serializers import ContactSerializer

from .models import Company


class CompanySerializer(serializers.ModelSerializer):
    contacts = ContactSerializer(many=True)

    class Meta:
        model = Company
        field = "__all__"
        read_only_fields = ["id", "created_at", "updated_at"]

    def create(self, validated_data: dict):
        contacts_data = validated_data.pop("contacts")

        company = Company.objects.create(**validated_data)

        for each_contact in contacts_data:
            contact, _ = Contact.objects.get_or_create(**each_contact)
            company.contacts.add(contact)

        return company

    def update(self, instance: Company, validated_data: dict):
        for key, value in validated_data.items():
            if key != "contacts":
                setattr(instance, key, value)
            if key == "contacts":
                for each_contact in value:
                    contact, _ = Contact.objects.get_or_create(**each_contact)
                    instance.contacts.add(contact)

        instance.save()

        return instance
