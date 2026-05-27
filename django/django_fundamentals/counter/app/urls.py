from django.urls import path
from . import views

urlpatterns =[
    path('', views.index),
    path('delete_session/', views.delete_session),


]
