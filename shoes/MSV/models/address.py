from django.db import models


class Address (models.Model):
    address_name = models.CharField(max_length=255)