from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(max_length=300)

    def __str__(s):
        return s.name

class Product(models.Model):
    name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField(max_length=300)
    img=models.ImageField(upload_to="images",default="")
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(s):
        return s.name
