from rest_framework import serializers

from contacts.models import Contact
from contacts.serializers import ContactSerializer
from equipments.models import Equipment
from equipments.serializers import EquipmentSerializer
from products.models import Product
from products.serializers import ProductSerializer

from .models import Company


class CompanySerializer(serializers.ModelSerializer):
    contacts = ContactSerializer(many=True)
    equipments = EquipmentSerializer(many=True)
    products = ProductSerializer(many=True)

    class Meta:
        model = Company
        fields = [
            "name",
            "description",
            "website",
            "contacts",
            "address",
            "city",
            "region",
            "products",
            "equipments",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]

    def create(self, validated_data: dict):
        contacts_data = validated_data.pop("contacts")
        equipments_data = validated_data.pop("equipments")
        products_data = validated_data.pop("products")

        company = Company.objects.create(**validated_data)

        for each_contact in contacts_data:
            contact = Contact.objects.create(**each_contact)
            company.contacts.add(contact)

        for each_equipment in equipments_data:
            equipment = Equipment.objects.create(**each_equipment)
            company.equipments.add(equipment)

        for each_product in products_data:
            product = Product.objects.get(**each_product)
            company.products.add(product)

        return company

    def update(self, instance: Company, validated_data: dict):
        for key, value in validated_data.items():
            if key != "contacts":
                if key != "equipments":
                    setattr(instance, key, value)
            if key == "contacts":
                for each_contact in value:
                    contact = Contact.objects.create(**each_contact)
                    instance.contacts.add(contact)
            if key == "equipments":
                for each_equipment in value:
                    equipment = Equipment.objects.create(**each_equipment)
                    instance.equipments.add(equipment)

        instance.save()

        return instance


class CreateUpdateCompanySerializer(serializers.ModelSerializer):
    contacts = ContactSerializer(many=True)
    equipments = EquipmentSerializer(many=True)
    products = serializers.ListField(child=serializers.IntegerField(min_value=1))

    class Meta:
        model = Company
        fields = [
            "name",
            "description",
            "website",
            "contacts",
            "address",
            "city",
            "region",
            "products",
            "equipments",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]

    def create(self, validated_data: dict):
        contacts_data = validated_data.pop("contacts")
        equipments_data = validated_data.pop("equipments")
        products_data = validated_data.pop("products")

        company = Company.objects.create(**validated_data)

        for each_contact in contacts_data:
            contact = Contact.objects.create(**each_contact)
            company.contacts.add(contact)

        for each_equipment in equipments_data:
            equipment = Equipment.objects.create(**each_equipment)
            company.equipments.add(equipment)

        for each_product in products_data:
            import ipdb

            ipdb.set_trace()
            product = Product.objects.get(pk=each_product)
            company.products.add(product)

        return company

    def update(self, instance: Company, validated_data: dict):
        for key, value in validated_data.items():
            if key != "contacts":
                if key != "equipments":
                    setattr(instance, key, value)
            if key == "contacts":
                for each_contact in value:
                    contact = Contact.objects.create(**each_contact)
                    instance.contacts.add(contact)
            if key == "equipments":
                for each_equipment in value:
                    equipment = Equipment.objects.create(**each_equipment)
                    instance.equipments.add(equipment)

        instance.save()

        return instance
