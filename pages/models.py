from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify

class Page(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 100, blank = False, null = False)
    contenido = RichTextField(default = '')
    orden = models.SmallIntegerField(default = 0, null = False, blank = False)
    slug = models.SlugField(blank = True, null = True)
    estado = models.BooleanField('Visible/Invisible', default = True)
    fecha_creacion = models.DateTimeField(auto_now_add = True)
    fecha_modificacion = models.DateTimeField(auto_now = True)
    
    class Meta:
        verbose_name = 'Pagina'
        verbose_name_plural = 'Paginas'
        ordering = ['orden', 'nombre']
        
    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre)
        super(Page, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.nombre
    
class Destacado(models.Model):
    id = models.AutoField(primary_key = True)
    titulo = models.CharField('Titulo', max_length = 100, blank = False, null = False)
    subtitulo = models.CharField('Subtitulo', max_length = 100, blank = False, null = False)
    orden = models.SmallIntegerField(default = 0, null = False, blank = False)
    estado = models.BooleanField('Activo/Inactivo', default = True)
    pagina = models.OneToOneField(Page, on_delete = models.DO_NOTHING, null = True, blank = True )
    fecha_creacion = models.DateTimeField(auto_now_add = True)
    fecha_modificacion = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name = 'Destacado'
        verbose_name_plural = 'Destacados'
        ordering = ['orden', 'titulo']
        
    def __str__(self):
        return self.titulo