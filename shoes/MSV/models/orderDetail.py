from django.db import models
from .order import Order
from .product import Product


class OrderDetail (models.Model):
    product = models.ForeignKey(Product, on_delete= models.CASCADE)
    order =models.ForeignKey(Order, on_delete= models.CASCADE)
    quantityOrdered = models.IntegerField(null=False)