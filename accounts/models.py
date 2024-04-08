from django.contrib.auth.models import AbstractUser
from django.core import validators
from django.db import models


# Create your models here
class User(AbstractUser):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.

    Username and password are required. Other fields are optional.
    """

    def __str__(self):
        return self.username
