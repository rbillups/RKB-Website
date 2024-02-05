from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='rkb-home'),
    path('about/', views.about, name='rkb-home-about'),
    path('products/', views.products, name='rkb-products')
]
