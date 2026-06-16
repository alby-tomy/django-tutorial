from django.shortcuts import render
from django.http import HttpResponse


def loginPage(request):
    return HttpResponse("Login Page")


def loginSuccess(request):
    return HttpResponse("Login Success")
