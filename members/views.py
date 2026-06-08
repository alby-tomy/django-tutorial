from django.shortcuts import render
from django.http import HttpResponse

def members(request):
    return HttpResponse("Hello world!")


def members1(request):
    return HttpResponse("Member 1")