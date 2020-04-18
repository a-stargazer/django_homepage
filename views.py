import requests

from django.shortcuts import render

pages = [
    "Home", 
    "Projects", 
    "About", 
    "Blog",
]

pages = [
    {"title": "Home",
    "file": "/"},
    {"title": "Projects",
    "file": "projects.html"},
    {"title": "About",
    "file": "about.html"},
    {"title": "Blog",
    "file": "blog.html"},
]

def homepage(request):
    print("index")
    context = {
        "title": pages[0]["title"],
        "pages": pages,
    }
    return render(request, "index.html", context)


def projects(request):
    print("projects")
    context = {
        "title": pages[1]["title"],
        "pages": pages,
    }
    return render(request, "projects.html", context)

def about(request):
    print("about")
    context = {
        "title": pages[2]["title"],
        "pages": pages,
    }
    return render(request, "about.html", context)

def blog(request):
    print("blog")
    context = {
        "title": pages[3]["title"],
        "pages": pages,
    }
    return render(request, "blog.html", context)



