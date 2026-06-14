from . import views
from django.urls import path

urlpatterns =[
    path('',views.index),
    path('create_dojo',views.create_dojo),
    path('create_ninga',views.create_ninga),
    #path('delete',views.delete),
]
