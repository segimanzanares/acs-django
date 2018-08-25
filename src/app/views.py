from django.shortcuts import render
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET"])
def users_index(request):
    return render(request, 'users/index.html')