from django.db import models


class Account(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    account_type = models.CharField(max_length=10)
    email = models.CharField(max_length=255)