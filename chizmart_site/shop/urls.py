from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import edit_product, delete_product

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('register/', views.register, name='register'),  # Registration page
    path('login/', views.user_login, name='login'),  # Login page
    path('products/', views.product_list, name='product_list'),  # product list page
    path('add_product/', views.add_product, name='add_product'),
    path('become-seller/', views.become_seller, name='become_seller'),
    path('product/<int:product_id>/edit/', edit_product, name='edit_product'),
    path('product/<int:product_id>/delete/', delete_product, name='delete_product'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
