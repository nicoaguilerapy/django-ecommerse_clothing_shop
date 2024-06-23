from django.shortcuts import render
from .models import  Category, ItemDetalle, ItemImagen
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from random import sample
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from django.shortcuts  import get_object_or_404
from django.db.models import Q
from .forms import *


class ItemListView(ListView):
    paginate_by = 12
    model = Item
    queryset = Item.objects.filter(visibility = True)
    
    def get_context_data(self, **kwargs):
        context = super(ItemListView, self).get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        print(context['item_list'])
        return context

    def get_queryset(self, *args, **kwargs):
        qs = Item.objects.filter(visibility = True)
        
        if self.request.GET.get('orden')=="mayor-menor":
            qs = Item.objects.filter(visibility = True).order_by('-price')
        
        if self.request.GET.get('orden')=="menor-mayor":
            qs = Item.objects.filter(visibility = True).order_by('price')  
            
        if self.request.GET.get('buscar'):
            return qs.filter(Q( title__icontains = self.request.GET.get('buscar') )
                             |Q( price__icontains = self.request.GET.get('buscar') )
                             |Q( description__icontains = self.request.GET.get('buscar') ), visibility = True).distinct()
        
        return qs
    
class CategoryListView(ListView):
    paginate_by = 12
    model = Item
    
    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        return context
    
    def get_queryset(self):
        
        qs = Item.objects.filter(visibility = True, categorias=self.kwargs['id'])
        
        if self.request.GET.get('orden')=="mayor-menor":
            qs = Item.objects.filter(visibility = True, categorias=self.kwargs['id']).order_by('-price')
        
        if self.request.GET.get('orden')=="menor-mayor":
            qs = Item.objects.filter(visibility = True, categorias=self.kwargs['id']).order_by('price')
            
        if self.request.GET.get('buscar'):
            return qs.filter(Q( title__icontains = self.request.GET.get('buscar') ) | Q( price__icontains = self.request.GET.get('buscar') ), visibility = True).distinct()
        
        return qs
    
class ItemDetailView(DetailView):
    model = Item

    def get_context_data(self, **kwargs):
        context = super(ItemDetailView, self).get_context_data(**kwargs)
        context['imagenes'] = ItemImagen.objects.filter(item = context['object'] )
        context['detalles'] = ItemDetalle.objects.filter(item = context['object'] )
        return context
    
class OfferListView(ListView):
    paginate_by = 12
    model = Item
    queryset = Item.objects.filter(visibility = True, offer = True)
    
    def get_context_data(self, **kwargs):
        context = super(OfferListView, self).get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        return context

    def get_queryset(self, *args, **kwargs):
        qs = Item.objects.filter(visibility = True, offer = True)
        
        if self.request.GET.get('orden')=="mayor-menor":
            qs = Item.objects.all().order_by('-price')
        
        if self.request.GET.get('orden')=="menor-mayor":
            qs = Item.objects.all().order_by('price')  
            
        if self.request.GET.get('buscar'):
            return qs.filter(Q( title__icontains = self.request.GET.get('buscar') )
                             |Q( price__icontains = self.request.GET.get('buscar') )
                             |Q( description__icontains = self.request.GET.get('buscar') ), visibility = True).distinct()
        
        return qs
    
