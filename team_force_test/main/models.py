from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    middle_name = models.CharField("Отчество", max_length=150, blank=True)




