
from django.contrib import admin
from django.urls import path
from . import views
app_name = 'user'
urlpatterns = [
    #path('', views.home),
    path('login', views.login_, name='login'),    path(
        'logout', views.logout_, name='logout'),

]
