from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from .models import BsuOfficeusers

class AuthBackend(BaseBackend):
    def authenticate(self, username=None, password=None):
        try:
            user = BsuOfficeusers.objects.get(user_name=username)
            if user is not None:
                if check_password(password, user.password):
                    return user
                else:
                    # Password does not match
                    return None
            else:
                # User was not found
                return None
        except BsuOfficeusers.DoesNotExist:
            # User was not found
            return None

    def get_user(self, user_id):
        try:
            return BsuOfficeusers.objects.get(pk=user_id)
        except BsuOfficeusers.DoesNotExist:
            return None