from django.db import models
from product.models import Product
from django.contrib.auth.models import User

class Cart(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

class Order(models.Model):
    totalBill=models.IntegerField()
    status=models.CharField(max_length=30,default="Processing")
    order_date=models.DateField(auto_now=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)