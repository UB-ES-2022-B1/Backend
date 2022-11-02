from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User

from clients.models import Client

class ClientBackend(ModelBackend):

    def authenticate(self, request, **kwargs):
        email = kwargs['email']
        password = kwargs['password']
        try:

            client = Client.objects.get(email=email)
            if client.failedLoginAttemps < 5:
                if client.check_password(password) is True:
                    if client.failedLoginAttemps > 0 and client.failedLoginAttemps < 5:
                        client.reset_failed_logins()
                    return client
                else:
                    client.increment_failed_login()
                    raise ValueError('Wrong password')
            else:
                raise ValueError('Block user')

        except Client.DoesNotExist:
            raise ValueError('User not exists')
