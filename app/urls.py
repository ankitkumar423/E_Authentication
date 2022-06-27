from django.contrib import admin
from django.urls import path,include
from app.views import *

urlpatterns = [
    path('', signup,name='signup'),
    path('signup', signup,name='signup'),
    path('login', login,name='login'),
    path('home', home,name='home'),
    path('changepass', changepass, name='changepass'),
    path('logout', logout,name='logout'),
]

