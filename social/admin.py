from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import *

class SocialResource(resources.ModelResource):
    class Meta:
        model = Social

class FactResource(resources.ModelResource):
    class Meta:
        model = Fact

class EmailResource(resources.ModelResource):
    class Meta:
        model = Email

class NumberResource(resources.ModelResource):
    class Meta:
        model = Number

class SocialAdmin(admin.ModelAdmin):
	readonly_fields = ('fecha_creacion','fecha_modificacion')
	search_fields = ['social']
	list_display = ('social', 'url',)
	resourse_class = SocialResource
	
	def get_readonly_fields(self, request, obj = None):
		if request.user.groups.filter(name="Personal").exists():
			return ('fecha_creacion','fecha_modificacion', 'slug', 'social')
		else:
			return ('fecha_creacion','fecha_modificacion')

class FactAdmin(admin.ModelAdmin):
	readonly_fields = ('fecha_creacion','fecha_modificacion')
	search_fields = ['fact']
	list_display = ('fact', 'value',)
	resourse_class = FactResource
	
	def get_readonly_fields(self, request, obj = None):
		if request.user.groups.filter(name="Personal").exists():
			return ('fecha_creacion','fecha_modificacion', 'slug', 'fact')
		else:
			return ('fecha_creacion','fecha_modificacion')
		
class EmailAdmin(admin.ModelAdmin):
	readonly_fields = ('fecha_creacion','fecha_modificacion')
	search_fields = ['email']
	list_display = ('category', 'email', 'estado',)
	resourse_class = EmailResource
	
	def get_readonly_fields(self, request, obj = None):
		if request.user.groups.filter(name="Personal").exists():
			return ('fecha_creacion','fecha_modificacion')
		else:
			return ('fecha_creacion','fecha_modificacion')
		
class NumberAdmin(admin.ModelAdmin):
	readonly_fields = ('fecha_creacion','fecha_modificacion')
	search_fields = ['number', 'category']
	list_display = ('category', 'number', 'whatsapp', 'estado',)
	resourse_class = Number
	
	def get_readonly_fields(self, request, obj = None):
		if request.user.groups.filter(name="Personal").exists():
			return ('fecha_creacion','fecha_modificacion')
		else:
			return ('fecha_creacion','fecha_modificacion')

admin.site.register(Social, SocialAdmin)
admin.site.register(Fact, FactAdmin)
admin.site.register(Email, EmailAdmin)
admin.site.register(Number, NumberAdmin)
