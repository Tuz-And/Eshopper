from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('404', views.error, name='error'),
    path('contact-us', views.contact_us, name='contact_us'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),
    path('dashboard', views.dashboard, name='dashboard'),

    
]
