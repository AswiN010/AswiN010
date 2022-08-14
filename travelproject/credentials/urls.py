from django.contrib import admin
from django.urls import path

from travelproject import settings
from . import views
from django.conf.urls.static import static
urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout',views.logout,name='logout')
]
