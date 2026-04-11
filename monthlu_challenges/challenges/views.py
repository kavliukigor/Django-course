from calendar import month
from django.http import HttpResponse,HttpResponseNotFound, HttpResponseRedirect, HttpResponseServerError
from django.shortcuts import render
from django.urls import reverse
from django.template.loader import render_to_string

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
    'december':'Already final'
}
# Create your views here.

def monthly_challenge_by_name(request,month):
    try:
        challenge_text=challenges[month]
        response_data=render_to_string('challenges/challenge.html')
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound('<h1>This month is not suported</h1>')


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
    for month in months:
        capitalized_month=month.capitalize()
        month_path=reverse('month-challenge', args=[month])
        list_item+=f"<li><a href='{month_path}'>{capitalized_month}</a></li>"
    response_data=f'<ul>{list_item}</ul>'
    return HttpResponse(response_data)