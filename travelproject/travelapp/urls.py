from django.contrib import admin
from django.urls import path

from travelproject import settings
from . import views
from django.conf.urls.static import static
urlpatterns = [
    path('', views.demo, name='demo')

]

