from django.db import models
from django.contrib.auth.models import User as DjangoUser

class Users(models.Model):
    # id = models.ForeignKey(DjangoUser,primary_key=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    username = models.CharField(max_length=255, default='')
    password = models.CharField(max_length=255)
    status = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)