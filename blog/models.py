from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify


class Post(models.Model):
    id = models.AutoField(primary_key = True)
    titulo = models.CharField('Titulo', max_length = 90, blank = False, null = False)
    descripcion = models.CharField('Descripcion', max_length = 150, blank = False, null = False)
    contenido = RichTextField()
    imagen = models.ImageField(upload_to = 'blog')
    estado = models.BooleanField('Activo/Inactivo', default = True)
    slug = models.CharField(max_length = 100, blank = True, null = True)
    fecha_creacion = models.DateField('Fecha de Creacion', auto_now = False, auto_now_add = True)
    fecha_modificacion = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        
    def save(self, *args, **kwargs):
        self.slug = slugify(self.titulo)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.titulo
