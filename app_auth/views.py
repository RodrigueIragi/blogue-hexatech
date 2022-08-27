from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import PermissionDenied

from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    if request.method=='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = User.objects.create_user(username=username, password=password)
            if user is not None:
                return redirect('login')
        
            else:
                messages.error(request, 'Creation de compte echoue')
                return render(request, 'user/register.html', {'form':form})
        else:
            return render(request, 'user/register.html', {'form':form})

        return render(request, 'user/register.html', {})

    form = RegisterForm()
    return render(request, 'user/register.html',{'form':form})

def login_form(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('account_user')

            else:
                messages.error(request, 'Authentification echoué !')
                return render(request, 'user/login.html', {'form':form})
        else:
            for field in form.errors:
                form[field].field.widget.attrs['class'] += ' is-invalid'
            return render(request, 'user/login.html', {'form':form})
            
    else:

        form = LoginForm()

        return render(request, 'user/login.html', {'form': form})


def logout_user(request):
    logout(request)

    return redirect('/')

@login_required
def account_user(request):
    has_perm = False
    if request.user.has_perm('account_user'):
        has_perm = True
        print('acces permit')

    return render(request, 'user/compte.html', {"has_perm":has_perm})