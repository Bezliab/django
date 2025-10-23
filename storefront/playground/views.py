from django.shortcuts import render
from django.http import HttpResponse


# Simple views for the playground app
def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def products(request):
    # Render a simple products page (template added)
    return render(request, "products.html")


def contact(request):
    return render(request, "contact.html")
