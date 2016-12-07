from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import UserForm

# Create your views here.

def home(request):
    return render(request, 'accounts/user_login.html')

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.set_password('password')
            f.save()
            return redirect('accounts:home')
        else:
            print(form.errors)
    else:
        form = UserForm()
    return render(request, 'accounts/register.html', {'form': form})

def user_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)

		if user:
			if user.is_active:
				login(request, user)
				return redirect('accounts:logado')
			else:
				messages.debug(request, 'Sua conta esta desativada.')
				return render(request, 'accounts/user_login.html')
		else:
			print('Login invalido, detalhes: {0}, {1}'.format(username, password))
			messages.error(request, 'Usuario ou senha invalido.')
			return render(request, 'accounts/user_login.html')
	else:
		return render(request, 'accounts/user_login.html', {})

@login_required
def logado(request):
    return render(request, 'accounts/logado.html')

@login_required
def sair(request):
    logout(request)
    return redirect('accounts:home')
