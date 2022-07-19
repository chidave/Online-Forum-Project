from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class AppUserBackend(ModelBackend):

    def authenticate(self, request, **kwargs):
        email = kwargs['email']
        password = kwargs['password']
        user_model = get_user_model()

        try:
            user = user_model.objects.get(email=email.lower())
        except user_model.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None

    def get_user(self, user_id):
        user_model = get_user_model()
        
        try:
            return user_model.objects.get(id=user_id)
        except user_model.DoesNotExist:
            return None