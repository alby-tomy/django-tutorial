from django.urls import path
from . import views

urlpatterns = [
    path("", views.members, name="members"),
    path("members1/", views.members1, name="members1"),
]
