from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    button_clicked = False
    return render( request, "main/index.html")

def form(request):
    return render( request, "main/form.html" )


def onboarding(request):
    return render( request, "main/onboarding.html" )

def detect(request):
    return render( request, "main/detect.html" )
