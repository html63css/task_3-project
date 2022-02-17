from django import forms
from django.urls import reverse_lazy
from django.contrib import auth
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from main.models import Account

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        users = User.objects.all()
        context['users'] = users
        if ('cat_selected' not in context):
            context['cat_selected'] = 0
        return context

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Username',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username','autocomplete':'off'}))
    password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password','autocomplete':'off'}))

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'main/log_in.html'

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Username',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username','autocomplete':'off'}))
    last_name = forms.CharField(label='Lastname',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Lastname','autocomplete':'off'}))
    email = forms.CharField(label='email',widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email','autocomplete':'off'}))
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password','autocomplete':'off'}))
    password2 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password','autocomplete':'off'}))
    class Meta:
        model = User
        fields = ('username', 'last_name', 'email', 'password1', 'password2')

class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'main/sign_up.html'
    def get_success_url(self, user=None):
        return reverse_lazy('log_in')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))
