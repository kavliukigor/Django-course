from calendar import month
from django.http import Http404,HttpResponseNotFound, HttpResponseRedirect, HttpResponseServerError
from django.shortcuts import render
from django.urls import reverse


challenges ={
    'january':'This works',
    'february':'Challenge complete!',
    'march':'Learn Django for at least 20 minutes',
    'april':'Walk at least 20k of steps per day',
    'may': 'BimBImbBImBIM',
    'june':'BAmBamBAMBAm',
    'july': 'Some text',
    'august':'Another text messgae',
    'september':'One more text',
    'november':'And one more sense less text',
    'october':'I am tired to write this',
    'december': None
}
# Create your views here.

def monthly_challenge_by_name(request,month):
    try:
        challenge_text=challenges[month]
        return render(request,'challenges/challenge.html',{
            'text':challenge_text,
            'title': month
        })
    except:
        raise Http404()


def monthly(request, month):
    months_list=list(challenges.keys())
    if month> len(challenges):
        return HttpResponseNotFound()
    redirect_month=months_list[month-1]
    redirect_path=reverse('month-challenge',args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def index(request):
    list_item=''
    months=list(challenges.keys())
    return render(request, 'challenges/index.html', {
        'months':months
    })