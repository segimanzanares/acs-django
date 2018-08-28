from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from app.models import User

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
        if user is not None:
            print("Password ok")
            auth_login(request, user)
            if request.GET.get('next') != None:
                return redirect(request.GET.get('next'))
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