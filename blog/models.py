from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify

class Category(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField('Nombre', max_length = 90, blank = False, null = False)
    slug = models.CharField(max_length = 100, blank = True, null = True)
    date_created = models.DateField('Fecha de Creacion', auto_now = False, auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Post(models.Model):
    id = models.AutoField(primary_key = True)
    title = models.CharField('Titulo', max_length = 90, blank = False, null = False)
    author = models.CharField('Autor', max_length = 90, blank = False, null = False, default= "Casa Fenix")
    content = RichTextField()
    description = models.TextField('Descripcion', blank = False, null = False)
    categories = models.ManyToManyField(Category, related_name='get_categories')
    image = models.ImageField(upload_to = 'post')
    status = models.BooleanField('Activo/Inactivo', default = True)
    slug = models.CharField(max_length = 100, blank = True, null = True)
    date_created = models.DateField('Fecha de Creacion', auto_now = False, auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)
    

    class Meta:
        verbose_name = 'Publicación'
        verbose_name_plural = 'Publicaciones'
        
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
    
    def get_categories(self):
        return " | ".join([str(p) for p in self.categories.all()])
    get_categories.short_description = 'Categorias'

    def __str__(self):
        return self.title

class Tag(models.Model):
    post = models.ForeignKey(Post, related_name='get_tagpost', default = None, on_delete = models.CASCADE)
    tag = models.CharField('Tag', max_length = 90, blank = False, null = False)

    def __str__(self):
        return self.tag
