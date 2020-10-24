from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('test/', views.test),
    path('loaddb/', views.loadDB),
   
]

