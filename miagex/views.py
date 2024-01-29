from django.http import HttpResponse
from django.shortcuts import render



def homepage(request):
    return render(request,"index.html")

def login(request):
    return render(request,"auth/login.html")

def register(request):
    return render(request,"auth/register.html")