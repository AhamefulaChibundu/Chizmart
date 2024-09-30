from django.db import models
from django.contrib.auth.models import User

# Seller Model
class Seller(models.Model):
    SELLER_TYPE_CHOICES = [
        ('Basic', 'Basic'),
        ('Premium', 'Premium'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=255)
    seller_type = models.CharField(max_length=50, choices=SELLER_TYPE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.business_name

# Product Model
class Product(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
