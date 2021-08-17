from django.shortcuts import render
from .models import Producto, Categoria, ProductoImagen, DetalleProducto
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


class ProductosListView(ListView):
    paginate_by = 12
    model = Producto
    queryset = Producto.objects.filter(estado = True)
    
    def get_context_data(self, **kwargs):
        context = super(ProductosListView, self).get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        return context

    def get_queryset(self, *args, **kwargs):
        qs = Producto.objects.filter(estado = True)
        
        if self.request.GET.get('orden')=="mayor-menor":
            qs = Producto.objects.filter(estado = True).order_by('-precio')
        
        if self.request.GET.get('orden')=="menor-mayor":
            qs = Producto.objects.filter(estado = True).order_by('precio')  
            
        if self.request.GET.get('buscar'):
            return qs.filter(Q( titulo__icontains = self.request.GET.get('buscar') )
                             |Q( precio__icontains = self.request.GET.get('buscar') )
                             |Q( descripcion__icontains = self.request.GET.get('buscar') ), estado = True).distinct()
        
        return qs
    
class CategoriaListView(ListView):
    paginate_by = 12
    model = Producto
    
    def get_context_data(self, **kwargs):
        context = super(CategoriaListView, self).get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        return context
    
    def get_queryset(self):
        
        qs = Producto.objects.filter(estado = True, categorias=self.kwargs['id'])
        
        if self.request.GET.get('orden')=="mayor-menor":
            qs = Producto.objects.filter(estado = True, categorias=self.kwargs['id']).order_by('-precio')
        
        if self.request.GET.get('orden')=="menor-mayor":
            qs = Producto.objects.filter(estado = True, categorias=self.kwargs['id']).order_by('precio')
            
        if self.request.GET.get('buscar'):
            return qs.filter(Q( titulo__icontains = self.request.GET.get('buscar') ) | Q( precio__icontains = self.request.GET.get('buscar') ), estado = True).distinct()
        
        return qs
    
class ProductoDetailView(DetailView):
    model = Producto

    def get_context_data(self, **kwargs):
        context = super(ProductoDetailView, self).get_context_data(**kwargs)
        context['imagenes'] = ProductoImagen.objects.filter(producto = context['object'] )
        context['detalles'] = DetalleProducto.objects.filter(producto = context['object'] )
        return context
    
class OfertasListView(ListView):
    paginate_by = 12
    model = Producto
    queryset = Producto.objects.filter(estado = True, oferta = True)
    
    def get_context_data(self, **kwargs):
        context = super(OfertasListView, self).get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        return context

    def get_queryset(self, *args, **kwargs):
        qs = Producto.objects.filter(estado = True, oferta = True)
        
        if self.request.GET.get('orden')=="mayor-menor":
            qs = Producto.objects.all().order_by('-precio')
        
        if self.request.GET.get('orden')=="menor-mayor":
            qs = Producto.objects.all().order_by('precio')  
            
        if self.request.GET.get('buscar'):
            return qs.filter(Q( titulo__icontains = self.request.GET.get('buscar') )
                             |Q( precio__icontains = self.request.GET.get('buscar') )
                             |Q( descripcion__icontains = self.request.GET.get('buscar') ), estado = True).distinct()
        
        return qs
    
@method_decorator(staff_member_required, name='dispatch')
class ProductoAdminListView(ListView):
	model = Producto
	paginate_by = 10
	template_name = "productos/admin/product_list.html"
		
	def get_queryset(self, *args, **kwargs):
		qs = Producto.objects.all()

		if self.request.GET.get('orden')=="mayor-menor":
			qs = Producto.objects.all().order_by('-precio')

		if self.request.GET.get('orden')=="menor-mayor":
			qs = Producto.objects.all().order_by('precio')
			
		if self.request.GET.get('orden')=="nuevo-viejo":
			qs = Producto.objects.all().order_by('fecha_creacion')
			
		if self.request.GET.get('orden')=="viejo-nuevo":
			qs = Producto.objects.all().order_by('-fecha_creacion') 

		if self.request.GET.get('buscar'):
			return qs.filter(Q( titulo__icontains = self.request.GET.get('buscar') )
							 |Q( precio__icontains = self.request.GET.get('buscar') )
							 |Q( descripcion__icontains = self.request.GET.get('buscar') ), estado = True).distinct()
			
		return qs
	
@method_decorator(staff_member_required, name='dispatch')
class ProductoAdminCreateView(CreateView):
	form_class = ProductoForm
	template_name = "productos/admin/product_form.html"
	success_url = reverse_lazy('admin_product_list')

@method_decorator(staff_member_required, name='dispatch')
class ProductoAdminUpdateView(UpdateView):
	model = Producto
	form_class = ProductoForm
	template_name = "productos/admin/product_form.html"
	template_name_suffix = '_update_form'
	success_url = reverse_lazy('admin_product_list')

@method_decorator(staff_member_required, name='dispatch')
class ProductoAdminDelete(DeleteView):
	model = Producto
	template_name = "productos/admin/producto_confirm_delete.html"
	success_url = reverse_lazy('admin_product_list')
    
        
    
        
    
            
            
        
        


    
