from datetime import datetime
from django.contrib import  messages
from  django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, update_session_auth_hash
from .forms import RegisterForm, EditAccountForm
from workspace.gmud.models import gmud

@login_required(login_url='/login')
def home(request):
    Gmud = gmud.objects.all()
    data = {}
    today = datetime.now()
    data['gmud_objects'] = Gmud
    data['today'] = today
    return render(request, 'home.html', data)
def sagebook(request):
    return render(request, 'sagebook.html')
def cetelembook(request):
    return render(request, 'cetelembook.html')
def sagebdbook(request):
    return render(request, 'sagebdbook.html')
def register(request):
    template_name = 'registration/register.html'
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(
                username=user.username, password=form.cleaned_data['password1']
            )
            login(request, user)
            if user.last_login.null:
                return redirect('changepassword')
            else:
                return redirect('home')

    else:
        form = RegisterForm()
    context = {
        'form': form
    }
    return render(request, template_name, context)
def userupdate(request):
    context = {}
    if request.method == 'POST':
        form = EditAccountForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save()
            form = EditAccountForm(instance=request.user)
            context['success'] = True
            return redirect('index')
    else:
        form = EditAccountForm(instance=request.user)
    context['form'] = form
    return render(request, 'registration/edit.html', context)

def changepassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Sua senha foi alterada com sucesso!')
            return redirect('index')
        else:
            messages.error(request, 'Senha inválida')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/changepassword.html', {'form': form})


