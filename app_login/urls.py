from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginPage, name='login'),
    path('logined/', views.loginSuccess, name='login_success'),
]