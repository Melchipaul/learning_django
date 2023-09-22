from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.template.loader import render_to_string
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
    'december': None
}
def index(request):
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {
        "months": months
    })

def monthly_challenge_by_number(request, month):
    try:
        months = list(monthly_challenges.keys())
        redirect_month = months[month-1]
        redirect_path = reverse("month-challenge", args=[redirect_month])
        return HttpResponseRedirect(redirect_path)
    except:
        raise Http404()

    
def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request,"challenges/challenge.html", {
            "month_name": month,
            "text": challenge_text})
    except:
        raise Http404()
