from . import views
from django.urls import path

urlpatterns =[
    path('books/',views.add_book),
    path('authors/',views.add_author),
    path('books/<int:id>/',views.book_detail ,name='book_detail'),
    path('authors/<int:id>/',views.author_detail ,name='author_detail'),
]