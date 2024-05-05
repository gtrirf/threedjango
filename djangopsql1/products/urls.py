from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.get_info, name='get_info'),
    path('products/<int:pk>/', views.get_products, name='get_products'),
    path('product/<int:pk>/', views.detail, name='detail'),
    path('add/', views.add_products, name='add_products'),
    path('update/<int:pk>/', views.update_products, name='update_products'),
    path('delete/<int:pk>/', views.delete_products, name='delete_products'),
]
