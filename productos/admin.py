from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Category, Item, CoverPage, ItemImagen, ItemDetalle


class ItemImagenAdmin(admin.StackedInline):
    model = ItemImagen

class DetalleItemAdmin(admin.StackedInline):
    model = ItemDetalle

class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category

class ItemResource(resources.ModelResource):
    class Meta:
        model = Item
        
class CoverPageResource(resources.ModelResource):
    class Meta:
        model = CoverPage
        
class CategoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'name')
    resourse_class = CategoryResource
    
    def get_readonly_fields(self, request, obj = None):
        readonly_fields = []
        if request.user.groups.filter(name="Personal").exists():
            readonly_fields.append('date_created')
            readonly_fields.append('slug')
        else:
            readonly_fields.append('date_created')

        return readonly_fields

class ItemAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ('title', 'visibility', 'date_created','date_updated',)
    list_display = ( 'id', 'title', 'visibility', 'priority', 'date_created','date_updated',)
    resourse_class = ItemResource
    readonly_fields = ('date_created','date_updated')
    inlines = [ItemImagenAdmin, DetalleItemAdmin]
    
    def get_readonly_fields(self, request, obj = None):
        readonly_fields = []
        if request.user.groups.filter(name="Personal").exists():
            readonly_fields.append('date_created')
            readonly_fields.append('date_updated')
            readonly_fields.append('slug')
        else:
            readonly_fields.append('date_created')
            readonly_fields.append('date_updated')
            
        return readonly_fields

@admin.register(ItemImagen)
class ItemImagenAdmin(admin.ModelAdmin):
    pass

@admin.register(ItemDetalle)
class DetalleItemAdmin(admin.ModelAdmin):
    pass
        
class CoverPageAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ('title', 'visibility' 'date_created','date_updated',)
    list_display = ( 'id', 'title', 'visibility', 'priority')
    resourse_class = CoverPageResource
    readonly_fields = ('date_created','date_updated')
    
    def get_readonly_fields(self, request, obj = None):
        readonly_fields = []
        readonly_fields.append('date_created')
        readonly_fields.append('date_updated')
            
        return readonly_fields


    
admin.site.register(Category, CategoryAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(CoverPage, CoverPageAdmin)
