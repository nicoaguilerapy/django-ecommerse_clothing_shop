from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from django.shortcuts  import get_object_or_404
from django.db.models import Q
from random import sample

class PostListView(ListView):
	paginate_by = 12
	model = Post
	
class PostDetailView(DetailView):
    model = Post

