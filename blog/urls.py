from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('contact/', views.contactUs, name='blog-contact'),
    path('profile/', views.companyProfile, name='blog-profile'),
]