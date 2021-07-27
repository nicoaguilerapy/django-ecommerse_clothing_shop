from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Categoria, Producto, Portada, ProductoImagen, DetalleProducto


class ProductoImagenAdmin(admin.StackedInline):
    model = ProductoImagen

class DetalleProductoAdmin(admin.StackedInline):
    model = DetalleProducto

class CategoriaResource(resources.ModelResource):
    class Meta:
        model = Categoria

class ProductoResource(resources.ModelResource):
    class Meta:
        model = Producto
        
class PortadaResource(resources.ModelResource):
    class Meta:
        model = Portada
        
class CategoriaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'nombre')
    resourse_class = CategoriaResource
    
    def get_readonly_fields(self, request, obj = None):
        readonly_fields = []
        if request.user.groups.filter(name="Personal").exists():
            readonly_fields.append('fecha_creacion')
            readonly_fields.append('slug')
        else:
            readonly_fields.append('fecha_creacion')

        return readonly_fields

class ProductoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ('titulo', 'estado', 'fecha_creacion','fecha_modificacion',)
    list_display = ( 'id', 'titulo', 'estado', 'orden', 'fecha_creacion','fecha_modificacion',)
    resourse_class = ProductoResource
    readonly_fields = ('fecha_creacion','fecha_modificacion')
    inlines = [ProductoImagenAdmin, DetalleProductoAdmin]
    
    def get_readonly_fields(self, request, obj = None):
        readonly_fields = []
        if request.user.groups.filter(name="Personal").exists():
            readonly_fields.append('fecha_creacion')
            readonly_fields.append('fecha_modificacion')
            readonly_fields.append('slug')
        else:
            readonly_fields.append('fecha_creacion')
            readonly_fields.append('fecha_modificacion')
            
        return readonly_fields

@admin.register(ProductoImagen)
class ProductoImagenAdmin(admin.ModelAdmin):
    pass

@admin.register(DetalleProducto)
class DetalleProductoAdmin(admin.ModelAdmin):
    pass
        
class PortadaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ('titulo', 'estado' 'fecha_creacion','fecha_modificacion',)
    list_display = ( 'id', 'titulo', 'estado', 'orden')
    resourse_class = PortadaResource
    readonly_fields = ('fecha_creacion','fecha_modificacion')
    
    def get_readonly_fields(self, request, obj = None):
        readonly_fields = []
        readonly_fields.append('fecha_creacion')
        readonly_fields.append('fecha_modificacion')
            
        return readonly_fields


    
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Portada, PortadaAdmin)

