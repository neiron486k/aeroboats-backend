from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    def __create_user(self, email, password=None, **extra_fields):
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)

    def create_user(self, email, password=None):
        self.__create_user(email, password)

    def create_superuser(self, email, password=None):
        extra_fields = {"is_staff": True, "is_superuser": True}

        self.__create_user(email, password, **extra_fields)
