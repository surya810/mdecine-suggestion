from django.urls import path
from disease_app import views

urlpatterns = [
    path('', views.home, name='home'),   
]
urlpatterns = [
    path('', views.home, name='home'),
    path('add_data/', views.add_data, name='add_data'),
]
urlpatterns = [
    path('', views.home, name='home'),
    path('add_data/', views.add_data, name='add_data'),
    path('import_data/', views.import_data, name='import_data'),
]
