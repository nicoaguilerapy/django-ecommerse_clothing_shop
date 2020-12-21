from django.contrib import admin
from .models import Post
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class PostResource(resources.ModelResource):
    class Meta:
        model = Post

class PostAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ('titulo', 'descripcion', 'fecha_creacion','fecha_modificacion',)
    list_display = ('titulo', 'estado', 'fecha_creacion','fecha_modificacion',)
    resourse_class = PostResource
    date_hierarchy = 'fecha_creacion'
    readonly_fields = ('fecha_creacion','fecha_modificacion')
    
    def get_readonly_fields(self, request, obj = None):
        if request.user.groups.filter(name="Personal").exists():
            return ('fecha_creacion','fecha_modificacion', 'slug')
        else:
            return ('fecha_creacion','fecha_modificacion')
        
admin.site.register(Post, PostAdmin)
