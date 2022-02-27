from django.db import models

# Create your models here.
class Product(models.Model):
    productname = models.CharField(max_length=120)
    productprice = models.CharField(max_length=120)
    productphoto = models.ImageField(upload_to = 'uploads/')
    productlink = models.URLField(max_length=250)