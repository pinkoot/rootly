from django.shortcuts import render
from django.http import HttpResponse

import datetime


def challenges_info(request):
    return HttpResponse("Таски")