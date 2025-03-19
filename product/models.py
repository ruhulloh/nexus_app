from django.db import models
from category.models import Region, Category, Brand
from user.models import Profile




class Product(models.Model):
    condition_types = [
        (1, "New"),
        (2, "Used"),
        (3, "Unpacked")
    ]

    status_types = [
        (1, "ACTIVE"),
        (2, "INACTIVE"),
        (3, "SOLD")
    ]

    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    location = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    condition = models.SmallIntegerField(choices=condition_types, default=1)
    status = models.SmallIntegerField(choices=status_types, default=1)
    price = models.IntegerField(null=True, blank=True)
    price_on_call = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.title

    
# Create your models here.

class ProductView(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    view_count = models.IntegerField(default=0)


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='media/')
    is_main = models.BooleanField(default=False)
