from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateAPIView,
    RetrieveDestroyAPIView,
)

from .permissions import IsAdmin, IsUser, IsViewer
from .mixin import CompaniesMixin
from .models import Company
from .serializers import CompanySerializer, CreateUpdateCompanySerializer


class ListCreateCompanyView(ListCreateAPIView):
    queryset = Company.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsViewer]
    serializer_class = CompanySerializer
    # serializer_map = {
    #    "GET": CompanySerializer,
    #    "POST": CreateUpdateCompanySerializer,
    # }


class RetrieveUpdateCompanyView(RetrieveUpdateAPIView):
    queryset = Company.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsUser]
    serializer_class = CompanySerializer


class RetrieveDestroyCompanyView(RetrieveDestroyAPIView):
    queryset = Company.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdmin]
    serializer_class = CompanySerializer
