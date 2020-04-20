import requests
from django.shortcuts import render

def homepage(request):
    context = {}
    return render(request, 'index.html', context)

def projects(request):
    context = {}
    return render(request, 'projects.html', context)

def about(request):
    context = {}
    return render(request, 'about.html', context)

def blog(request):
    context = {}
    return render(request, 'blog.html', context)

