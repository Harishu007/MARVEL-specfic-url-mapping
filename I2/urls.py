from I2.views import *
from django.urls import path
app_name='vinay'

urlpatterns=[
    path('wanda/',wanda,name='wanda'),
    path('vision/',vision,name='vision'),
    
]