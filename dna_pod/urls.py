from django.urls import path
from . import views


urlpatterns=[
    path('', views.dna_page, name='dna_page')
]