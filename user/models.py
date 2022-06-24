from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    MANAGER = 1
    ADMINISTRATOR = 2

    ROLE_CHOICES = (
        (MANAGER, 'Manager'),
        (ADMINISTRATOR, 'Administrator'),
    )
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES,
                                            blank=True,
                                            null=True)
