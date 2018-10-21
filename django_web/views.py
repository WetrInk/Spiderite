from django.http import HttpResponse
from django.shortcuts import render, redirect
from spider_task import spider_main as sp

def index(request):
    return render(request, "django_web/index.html")
    
