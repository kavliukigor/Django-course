from calendar import month
from django.http import HttpResponse,HttpResponseNotFound, HttpResponseRedirect, HttpResponseServerError
from django.shortcuts import render

challenges ={
    'january':'This works',
    'february':'Challenge complete!',
    'march':'Learn Django for at least 20 minutes',
    'may': 'BimBImbBImBIM',
    'june':'BAmBamBAMBAm'
}
# Create your views here.

def monthly_challenge_by_name(request,month):
    challenge_text=challenges[month]
    return HttpResponse(challenge_text)

def monthly(request, month):
    months_list=list(challenges.keys())
    redirect_month=months_list[month]
    return HttpResponseRedirect('/challenges/' + redirect_month)