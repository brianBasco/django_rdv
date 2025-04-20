
from django.urls import path
from . import views

urlpatterns = [
    path('authorize/', views.authorize, name='authorize'),
    path('oauth2callback/', views.oauth2callback, name='oauth2callback'),
    path('contacts/', views.contacts, name='contacts'),
]