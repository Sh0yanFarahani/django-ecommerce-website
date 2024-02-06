from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'books'

urlpatterns = [
    path("", views.BookListView.as_view(), name='list-view'),
    path("<uuid:pk>", views.BookDetailView.as_view(), name="book_detail"),
    path('search/', views.SearchResultView.as_view() ,name='search')
]
