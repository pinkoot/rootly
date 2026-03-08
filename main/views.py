from django.shortcuts import render
from django.http import HttpResponse

import datetime


def main_info(request):
    return render(request, 'index.html')


def main_about(request):
    return render(request, 'about.html')

def main_challenges(request):
    return render(request, 'challenges.html')