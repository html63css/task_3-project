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
    GET = request.GET
    user_status = {}
    for i in Account.objects.all().values_list('data_id', flat=True):
        user_status[User.objects.get(id=i)] = Account.objects.get(data_id=i).status
        print(Account.objects.get(data_id=i).status)
    context = {
    'user_status' : user_status,
    }

    if ('action' in GET) and ('id_user' in GET):
        GET_list_id_user = GET.getlist('id_user')
        if (GET['action'] == 'Block'):
            for i in GET_list_id_user:
                d = User.objects.get(id=i)
                print("BLOCK USER:  %s" %d)

        if (GET['action'] == 'Unblock'):
            for i in GET_list_id_user:
                d = User.objects.get(id=i)
                print("UNBLOCK USER:  %s" %d)

        if (GET['action'] == 'Delete' and GET['id_user']):
            for i in GET_list_id_user:
                d = User.objects.get(id=i)
                d.delete()

    return render(request, 'main/users_table.html', { 'context':user_status} )
