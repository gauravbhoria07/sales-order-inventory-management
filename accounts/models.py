from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):

    email= models.EmailField(unique = True)

    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        SALES_USER = "SALES_USER" ,"Sales User"

    role= models.CharField(
        max_length = 20,
        choices= Role.choices,
        default = Role.SALES_USER
    )

    def __str__(self):
        return self.username
