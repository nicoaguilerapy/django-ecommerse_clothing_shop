from django.contrib import admin
from .models import Post, Category, Tag
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class PostTagAdmin(admin.StackedInline):
    model = Tag

#category
class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category

class CategoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ('name', 'date_created',)
    list_display = ('name', 'date_created',)
    resourse_class = CategoryResource
    date_hierarchy = 'date_created'
    readonly_fields = ('date_created','date_updated')
    
    def get_readonly_fields(self, request, obj = None):
        if request.user.groups.filter(name="Personal").exists():
            return ('date_created','date_updated', 'slug')
        else:
            return ('date_created','date_updated')
        

#posts
class PostResource(resources.ModelResource):
    class Meta:
        model = Post

class PostAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ('title', 'description', 'date_created','date_updated',)
    list_display = ('title', 'status', 'get_categories','date_created','date_updated',)
    resourse_class = PostResource
    inlines = [PostTagAdmin]
    date_hierarchy = 'date_created'
    readonly_fields = ('date_created','date_updated')
    
    def get_readonly_fields(self, request, obj = None):
        if request.user.groups.filter(name="Personal").exists():
            return ('date_created','date_updated', 'slug')
        else:
            return ('date_created','date_updated')


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)