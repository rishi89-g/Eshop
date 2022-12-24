from django.db import models
from .category import Category

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField(default=0.00)
    Category = models.ForeignKey(Category , on_delete=models.CASCADE, default=1)
    discription = models.CharField(max_length=200)
    image = models.ImageField(upload_to='Uploads/Products/')
