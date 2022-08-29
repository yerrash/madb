from django.urls import path
from . import views

urlpatterns = [
    path("companies/", views.ListCreateCompanyView.as_view()),
    path("companies/<pk>/", views.RetrieveUpdateCompanyView.as_view()),
    path("companies/delete/<pk>", views.RetrieveDestroyCompanyView.as_view()),
]
