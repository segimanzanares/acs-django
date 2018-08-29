from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from app.models import User
from app.models import Role
from app.forms import UserForm

@require_http_methods(["GET", "POST"])
def login(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect(reverse('users.index'))
        return render(request, 'auth/login.html')
    else:
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        next = request.POST['_next']
        print(next)
        if user is not None:
            auth_login(request, user)
            if next != '':
                return redirect(next)
            return redirect(reverse('users.index'))
        else:
            return redirect(reverse('login'))

def logout(request):
    auth_logout(request)
    return redirect(reverse('login'))

@login_required
@require_http_methods(["GET"])
def users_index(request):
    users = User.objects.all()[:20]
    context = {
        'users': users
    }
    return render(request, 'users/index.html', context)

@login_required
@require_http_methods(["GET", "POST"])
def users_create(request):
    from django.conf import settings
    form_type = settings.GLOBAL_SETTINGS['FORM_CREATE']
    readonly = ''
    disabled = ''
    if form_type == settings.GLOBAL_SETTINGS['FORM_SHOW']:
        readonly = 'readonly'
        disabled = 'disabled'
    context = {
        'readonly': readonly,
        'disabled': disabled,
        'form_type': form_type,
        'roles': Role.objects.all()
    }
    context.update(settings.GLOBAL_SETTINGS)
    if request.method == 'GET':
        form = UserForm()
        context.update({'form': form})
        return render(request, 'users/form.html', context)
    else:
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User()
            new_user.first_name = form.cleaned_data.get('first_name')
            new_user.last_name = form.cleaned_data.get('last_name')
            new_user.email = form.cleaned_data.get('email')
            new_user.password = form.cleaned_data.get('password')
            new_user.role = form.cleaned_data.get('role')
            new_user.save()
            return redirect(reverse('users.index'))
        else:
            context.update({'form': form})
            return render(request, 'users/form.html', context)