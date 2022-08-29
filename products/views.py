from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .permissions import IsAdmin
from .models import Product
from .serializers import ProductSerializer


class ListCreateProductView(ListCreateAPIView):
    queryset = Product.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdmin]
    serializer_class = ProductSerializer


class RetrieveUpdateDestroyProductView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdmin]
    serializer_class = ProductSerializer
