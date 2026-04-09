from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse('This works!')

def feb(request):
    return HttpResponse('Challenge complete!')