from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        "title": "Home",
        "content": "Главная страница магизина - HOME",
        "list": ["first", "second"],
        "dict": {"di": 23},
        "bool": True,
    }

    return render(request, "main/index.html", context)


def about(request):
    return HttpResponse("About page")
