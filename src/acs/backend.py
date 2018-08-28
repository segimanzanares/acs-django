from django.contrib.auth.hashers import check_password
from django.core.exceptions import ObjectDoesNotExist
from app.models import User

class AcsBackend:
    
    def authenticate(self, request, email=None, password=None):
        try:
            user = User.objects.get(email=email)
            pwd_valid = check_password(password, user.password)
            if pwd_valid:
                return user
            return None
        except ObjectDoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None