from django.urls import path
from . import views

urlpatterns = [
    path("users/", views.ListCreateUserView.as_view()),
    path("users/<pk>/", views.RetrieveUpdateUserView.as_view()),
    path("login/", views.LoginUserView.as_view()),
]
