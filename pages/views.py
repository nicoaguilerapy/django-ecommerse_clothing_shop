from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Page
from django.views.generic.detail import DetailView

class PageDetailView(DetailView):
    model = Page
    