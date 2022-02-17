from django.http.response import HttpResponse
from django.shortcuts import render
from .templates.forms import  *
from .models import *
from django.contrib.auth import logout

def home(request):
    context = {
    'title':'Home page'
    }
    return render(request, 'main/home.html', {'context':context})

def users_table(request):
    GET = request.GET

    if ('action' in GET) and ('id_user' in GET):
        GET_list_id_user = GET.getlist('id_user')
        if (GET['action'] == 'Block'):
            for i in GET_list_id_user:
                d = Account.objects.get(data_id=i)
                d.set_status('Block')
<<<<<<< HEAD
                if (int(i) == int(request.user.id)):
                    logout(request)
=======
                print("BLOCK USER:  %s" %d.status)
>>>>>>> 0ca27cc1f93f47fae5a4a62753172412a7d35f33
        if (GET['action'] == 'Unblock'):
            for i in GET_list_id_user:
                d = Account.objects.get(data_id=i)
                d.set_status('Unblock')
<<<<<<< HEAD
=======
                print("UNBLOCK USER:  %s" %d.status)
>>>>>>> 0ca27cc1f93f47fae5a4a62753172412a7d35f33
        if (GET['action'] == 'Delete' and GET['id_user']):
            for i in GET_list_id_user:
                d = Account.objects.get(data_id=i)
                d.delete()

    user_status = {}
    for i in Account.objects.all().values_list('data_id', flat=True):
        user_status[User.objects.get(id=i)] = Account.objects.get(data_id=i).status
    context = {
    'user_status' : user_status,
    }
    return render(request, 'main/users_table.html', { 'context':user_status} )
