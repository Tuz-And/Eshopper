from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('404', views.error, name='error'),
    path('contact-us', views.contact_us, name='contact_us'),

    
]
