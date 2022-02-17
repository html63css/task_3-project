from django import forms
from main.models import Account
from django.contrib import auth
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from main.models import Account
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        users = User.objects.all()
        context['users'] = users
        if ('cat_selected' not in context):
            context['cat_selected'] = 0
        return context

# class AuthenticationFormUser(AuthenticationForm):
#     def confirm_login_allowed(self, user):
#         if (1):
#             raise ValidationError(
#             ("This account is blocked."),
#             code = 'block'
#             )

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Username',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username','autocomplete':'off'}))
    password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password','autocomplete':'off'}))
    def confirm_login_allowed(self, user):
        if (Account.objects.get(data_id=user.id).status == 'Block'):
            raise ValidationError(
            ("This account is blocked."),
            code = 'block'
            )

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

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'main/sign_up.html'
    def get_success_url(self, user=None):
        return reverse_lazy('log_in')
