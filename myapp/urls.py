from django.urls import path
from .views import *

urlpatterns = [

    path('index/',index),
    path('home/',home),
    path('date/',date1),
    path('index1/',index1),
    path('veg/',veg)
]