from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


# Clase abstracta que se encarga de crear el usuario base con los atributos por defecto de django
class UserManager(BaseUserManager):
    def create_user(self, email, birthdate,name,surname, password=None):
        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=birthdate,
            name=name,
            surname=surname
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

# Clase cliente con los atributos por defecto.
class Client(AbstractBaseUser):
    email = models.EmailField(
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    country = models.CharField("Country", max_length=30)
    birthdate = models.DateField("Birth Date")
    failedLoginAttemps = models.IntegerField("Number of Failed logins", default=0)
    objects = UserManager()

    USERNAME_FIELD = 'email'

    def increment_failed_login(self):
        self.failedLoginAttemps += 1

    def reset_failed_logins(self):
        self.failedLoginAttemps = 0
