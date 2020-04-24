from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.hashers import PBKDF2PasswordHasher
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout

from .models import *
from .forms import *
from .gamemode_utilities import *

# Create your views here.

def get_standard_data(request):
    data = {
        'logged_in' : request.user.is_authenticated,
        'user' : request.user,
        'servers': get_game_servers()
    }
    return data

def get_game_servers():
    servers = GameServer.objects.order_by('-server_players')
    
    return {'servers': servers}

def index(request):
    
    form = LoginForm()
    if (request.user.is_authenticated):
        return render(request, 'servers.html', {'form': form, 'data': get_standard_data(request)})
    else:
        return render(request, 'login.html', {'form': form, 'data': get_standard_data(request)})

def login_view(request):

    if (request.method == "POST"):
        form = LoginForm(request.POST)
        if (form.is_valid()):
            username, password = form.cleaned_data['username'], form.cleaned_data['password']
            user = authenticate(request, username=username, password = password)
            if (user):
                login(request, user)

                return HttpResponseRedirect('/')
            else:
                return HttpResponseRedirect('/')
    else:
        if (request.user.is_authenticated):
            print(request.user)
            return HttpResponseRedirect('/')
        form = LoginForm()
    
        return render(request, 'login.html', {'form': form, 'data': get_standard_data(request)})
   

def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")

def register(request):
    if (request.method == "POST"):
        form = RegisterForm(request.POST)
        if (form.is_valid()):
            data = form.cleaned_data
            user = User.objects.create_user(data['username'], data['email'], data['password'])
            user.save()
            return HttpResponseRedirect('/')
    else:
        form = RegisterForm()
        return render(request, 'register.html', {'form': form, 'data': get_standard_data(request)})

def validate_password(login_details):
    email = login_details['email']
    password = login_details['password']

    ency = PBKDF2PasswordHasher()
    ency.digest
    pass_hshed = ency.encode()
    return pass_hshed

def add_server(request):
    if (request.method == "POST"):
        form = GameServerForm(request.POST)
        if form.is_valid():
            server_name, server_address, server_max_players = form.cleaned_data['server_name'], form.cleaned_data['server_address'], \
                form.cleaned_data['server_max_players']
            gs = GameServer()
            gs.server_name = server_name
            gs.server_max_players = server_max_players
            gs.server_address = server_address
            gs.server_gamemode = 0
            gs.server_players = 0
            gs.server_gamemode_name = get_gamemode_name(gs.server_gamemode)
            gs.save()
            return HttpResponseRedirect('/')
    else:
        form = GameServerForm()
        return render(request, 'add_server.html', {'form': form, 'data': get_standard_data(request)})
