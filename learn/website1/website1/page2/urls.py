# ----------------------------------
# This script is used for ...
# Created by winadm
# Version 0.1
# Examples
# ...
# ----------------------------------
from django.urls import path
from . import views
app_name = 'page2'
urlpatterns = [
    path('', views.index, name='index'),
]