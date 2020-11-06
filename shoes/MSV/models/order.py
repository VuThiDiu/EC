from django.db import models
from .customer import Customer



class Order (models.Model):
    customer = models.ForeignKey(Customer, on_delete= models.CASCADE)
    require_date = models.DateField(auto_now=True)
    shipped_date = models.DateField(auto_created=False, null=True)
    status = models.CharField(max_length=255)
    comment = models.CharField(max_length=255)