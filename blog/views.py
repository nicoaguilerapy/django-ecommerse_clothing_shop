from django.shortcuts import render, get_object_or_404
from .models import *
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
    paginate_by = 5
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        tags = Tag.objects.all()
        posts = Post.objects.filter(status = True)
        categories = Category.objects.all()
        context['tags'] = tags
        context['posts'] = posts
        context['categories'] = categories
        return context

    def get_queryset(self):
        qs = Post.objects.filter(status = True)
        if self.request.GET.get('buscar'):
            qs1 = qs.filter(Q( title__icontains = self.request.GET.get('buscar') )
                             |Q( description__icontains = self.request.GET.get('buscar') )
                             |Q( content__icontains = self.request.GET.get('buscar') ), status = True).distinct()
            print(qs1)

            tagqs = Tag.objects.filter(tag__icontains = self.request.GET.get('buscar'))
            print(tagqs)
            qs2 = qs.filter(get_tagpost__in = tagqs).distinct()
            print(qs2)
            qs = qs1 | qs2
        
        if self.request.GET.get('categoria'):
            qs = qs.filter(status = True, categories__in = self.request.GET.get('categoria')).distinct()

        if self.request.GET.get('tag'):
            qs = qs.filter(status = True, get_tagpost__in = self.request.GET.get('tag')).distinct()

        


        return qs    

    
class PostDetailView(DetailView):
    model = Post
    
    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        tags = Tag.objects.filter(post = context['object'] )
        posts = Post.objects.filter(status = True)
        context['tags'] = tags
        context['posts'] = posts
        return context

