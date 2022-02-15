from django.http.response import HttpResponse
from django.shortcuts import render
from .templates.forms import  *
from .models import *


def home(request):
    context = {
    'title':'Home page'
    }
    return render(request, 'main/home.html', {'context':context})
