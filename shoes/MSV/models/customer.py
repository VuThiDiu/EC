from django.db import models
from .account import Account 
from .address import Address


# name file 
def name_image(instance, filename):
    ex = filename.split('.')[-1];
    return "profile_shop" + "{}.{}".format(instance.account.userName, ex)

class Customer (models.Model):
    account = models.ForeignKey(Account, on_delete= models.CASCADE)
    phone = models.CharField(max_length=30)
    name = models.CharField(max_length=255)
    profile_picture = models.ImageField(upload_to = name_image)
    address = models.ManyToManyField(Address)
