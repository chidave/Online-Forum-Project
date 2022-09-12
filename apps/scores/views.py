from django.shortcuts import redirect, render
from django.http import HttpRequest
from datetime import datetime, timedelta

from .helper import get_data

# Create your views here.
def yesterdayResults(request: HttpRequest):
    yesterday = datetime.today() - timedelta(1)
    yesterday_date = yesterday.isoformat("|").split("|")[0]

    fixtures = get_data(yesterday_date, 0)
    context = {'fixtures': fixtures, 'date': yesterday_date}
    return render(request, "scores/yesterdayResults.html", context)

def todayFixtures(request: HttpRequest):
    today = datetime.today()
    today_date = today.isoformat("|").split("|")[0]

    fixtures = get_data(today_date, 1)
    context = {'fixtures': fixtures, 'date': today_date}
    return render(request, "scores/todayFixtures.html", context)