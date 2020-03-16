from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from .models import BsuOfficeusers
import datetime

class AuthBackend(BaseBackend):
    def authenticate(self, username=None, password=None):
        try:
            user = BsuOfficeusers.objects.get(user_name=username)
            if user is not None:
                # Check for valid time
                if self.check_failed_login_timer(user_failedlogin=user.failedlogin):
                    if check_password(password, user.password):
                        # Successful login
                        user.failedremain = 5
                        user.save()
                        return user
                    else:
                        # Password does not match
                        if user.failedremain <= 0:
                            user.failedlogin = datetime.datetime.now()
                        else:
                            user.failedremain = user.failedremain - 1
                        user.save()
                        return None
                else:
                    # Forced login timer has not expired
                    raise ValueError
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

    def check_failed_login_timer(self, user_failedlogin):
        # Check if the user_failedlogin time is greater than 5 minutes in the past
        # returns True if the time is greater than or equal 5 minutes in the past
        # returns False if the time is less than 5 minutes in the past

        # If user_failedlogin is null, the failedlogin time has not been set and should return true
        user_time = user_failedlogin
        current_minus_five = datetime.datetime.now() - datetime.timedelta(minutes=5)
        if user_time is not None:
            if user_time > current_minus_five:
                # Within the past five minutes, failed to wait required time
                return False
            else:
                # More than five minutes in the past, succeeded to wait the required time
                return True
        else:
            return True
