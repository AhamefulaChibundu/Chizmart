from django import forms
from django.contrib.auth.models import User
from .models import Product

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput),
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image']

from django import forms
from .models import Seller, Product

# Seller Registration Form
class SellerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = ['business_name', 'seller_type']
