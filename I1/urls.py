from I1.views import *
from django.urls import path
app_name='vinay'

urlpatterns=[
    path('ironman/',ironman,name='ironman'),
    path('spider/',spider,name='spider'),
    
]