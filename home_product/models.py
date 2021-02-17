from django.db import models

# Create your models here.


class Product (models.Model):
    product_name = models.CharField(max_length=50)
    product_image = models.ImageField(upload_to='product_images/')
    product_details = models.CharField(max_length=255)
    #prise =
