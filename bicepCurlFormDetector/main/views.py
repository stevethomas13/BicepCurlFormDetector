from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render( request, "main/index.html")

def form(request):
    return render( request, "main/form.html" )