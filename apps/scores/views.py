from django.shortcuts import redirect, render
from django.http import HttpRequest

from .helper import get_data

# Create your views here.
def yesterdayResults(request: HttpRequest):
    fixtures = get_data()
    context = {'fixtures': fixtures}
    return render(request, "scores/yesterdayResults.html", context)

def todayFixtures(request: HttpRequest):
    context = {}
    return render(request, "scores/todayFixtures.html", context)