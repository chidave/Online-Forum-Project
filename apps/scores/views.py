from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse

from .helper import get_data

# Create your views here.
def index(request: HttpRequest):
    fixtures = get_data()
    context = {'fixtures': fixtures}
    return render(request, "scores/scoresIndex.html", context)


def getData(request: HttpRequest):
    get_data()
    return redirect('scores')