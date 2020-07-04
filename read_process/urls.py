from django.urls import path
from . import views


urlpatterns=[
    path('', views.read_process, name='read_process')
]