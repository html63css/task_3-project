from django.http.response import HttpResponse
from django.shortcuts import render
from .templates.forms import  *
from .models import *


def home(request):
    context = {
    'title':'Home page'
    }
    return render(request, 'main/home.html', {'context':context})

def users_table(request):
    context = User.objects.all()
    return render(request, 'main/users_table.html', { 'context':context} )
