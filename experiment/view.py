from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from experiment.models import News

def home(request):
    return render(request, "experiment/home.html")