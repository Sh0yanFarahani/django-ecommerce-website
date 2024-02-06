from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Book
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q 

# Create your views here.

class BookListView(LoginRequiredMixin, ListView):
    model = Book
    login_url = "account_login"   

class BookDetailView(LoginRequiredMixin,DetailView):
    model = Book
    login_url = "account_login"   

class SearchResultView(LoginRequiredMixin, ListView):
    model = Book
    login_url = "account_login" 
    template_name = 'books/search_results.html'
    def get_queryset(self):
        query = self.request.GET.get("q")
        return Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )
