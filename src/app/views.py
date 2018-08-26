from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required

@require_http_methods(["GET"])
def login(request):
    return render(request, 'auth/login.html')

@require_http_methods(["GET"])
def users_index(request):
    return render(request, 'users/index.html')