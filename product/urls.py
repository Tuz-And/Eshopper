from django.urls import path, include
from . import views

urlpatterns = [
    # path('', views.product, name='product'),
    path('', views.cart2, name='cart2'),
    path('<int:product_id>/', views.cart, name='cart'),

   
]