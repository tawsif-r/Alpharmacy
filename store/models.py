from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Finaled_order(models.Model):
    STATUS = (
        ('Pending','pending'),
        ('Out for delivery','Out for delivery'),
        ('Delivered','Delivered'),
    )
    name = models.CharField(max_length=100,null=True)
    email = models.CharField(max_length=100,null=True)
    address = models.CharField(max_length=500,null=True)
    order_description = models.CharField(max_length=500,null=True)
    status = models.CharField(max_length=100,null=True,choices=STATUS)
    total= models.CharField(max_length=20,null=True)
    def __str__(self):
        return self.name