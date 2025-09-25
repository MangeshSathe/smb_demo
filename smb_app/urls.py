from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('', views.book_table, name="book_table"),
    path('book_list', views.book_list, name="book_list"),
    path('book_create', views.book_create, name="book_create"),
    path('book_edit/<int:pk>', views.book_edit, name="book_edit"),
    path('book_delete/<int:pk>', views.book_delete, name="book_delete")
    
]
