from django.urls import path
from . import views
from Ecom.controller import *

urlpatterns= [

    path('',views.home , name="home"),
    path('productviwes/<str:myslug>',views.productviwes , name="productviwes"),
    path('register',views.register , name="register")
    
]