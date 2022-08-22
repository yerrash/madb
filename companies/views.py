from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

from .permissions import IsAdmin, IsUser
from .models import Company
from .serializers import CompanySerializer


class ListCreateCompanyView(ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class RetrieveUpdateCompanyView(RetrieveUpdateAPIView):
    queryset = Company.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsUser]
    serializer_class = CompanySerializer
