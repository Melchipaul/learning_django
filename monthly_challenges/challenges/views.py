from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
# Create your views here.

monthly_challenges = {
    'january': 'Eat no meat for the entire month!',
    'february': 'Walk for least 20 minutes every day!',
    'march': 'Learn Django for least 20 minutes every day!',
    'april': 'Walk for least 20 minutes every day!',
    'may': 'Eat no meat for the entire month!',
    'june': 'Walk for least 20 minutes every day!',
    'july': 'Eat no meat for the entire month!',
    'august': 'Walk for least 20 minutes every day!',
    'september': 'Eat no meat for the entire month!',
    'october': 'Walk for least 20 minutes every day!',
    'november': 'Eat no meat for the entire month!',
    'december': 'Walk for least 20 minutes every day!'
}
def index(request):
    response_data = ""
    for  month in monthly_challenges.keys():
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        response_data += f"<li><h1><a href='{month_path}'>{capitalized_month}</a></h1></li>"
    body_data = f"<ul>{response_data}</ul>"
    return HttpResponse(body_data)

def monthly_challenge_by_number(request, month):
    try:
        months = list(monthly_challenges.keys())
        redirect_month = months[month-1]
        redirect_path = reverse("month-challenge", args=[redirect_month])
        return HttpResponseRedirect(redirect_path)
    except:
        return HttpResponseNotFound("<h1>Invalid month</h1>")

    
def monthly_challenge(request, month):
    try:
        response_data = f"<h1> {monthly_challenges[month]} </h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>Invalid month</h1>")
