from django.db import models
from .category import Category


class Product (models.Model):
    product_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.IntegerField(null=False)
    quantity_In_Stock = models.IntegerField(null=False)
    saleOff= models.IntegerField(null=True, default=0)
    category = models.ForeignKey(Category, on_delete= models.CASCADE)
    product_picture = models.ImageField()
