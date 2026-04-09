from django.http import HttpResponse,HttpResponseNotFound
from django.shortcuts import render

# Create your views here.

def january(request):
    return HttpResponse('This works!')

def february(request):
    return HttpResponse('Challenge complete!')

def march(request):
    return HttpResponse('Learn Django for at least 20 minutes')

def monthly(request, month):
    challenge_text = None
    if month == 'january':
        challenge_text = 'This works'
    elif month == 'january':
        challenge_text = 'Challenge complete!'
    elif month == 'january':
        challenge_text = 'Learn Django for at least 20 minutes'
    else:
        challenge_text='Not supported month'
        return HttpResponseNotFound()
    return HttpResponse(challenge_text)