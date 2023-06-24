from django.urls import path
from disease_app import views

urlpatterns = [
    path('', views.home, name='home'),
]