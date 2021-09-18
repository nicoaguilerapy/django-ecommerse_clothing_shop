from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Page

class PageResource(resources.ModelResource):
    class Meta:
        model = Page
    

class PagesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
	readonly_fields = ('date_updated', 'date_created')
	list_display = ('title', 'order', 'status', 'date_created','date_updated',)
	resourse_class = PageResource
	
	def get_readonly_fields(self, request, obj = None):
		if request.user.groups.filter(name="Personal").exists():
			return ('date_created','date_updated', 'slug')
		else:
			return ('date_created','date_updated')

admin.site.register(Page, PagesAdmin)
