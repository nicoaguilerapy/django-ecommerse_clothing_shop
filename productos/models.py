from django.db import models
from django.utils.text import slugify

class CoverPage(models.Model):
    id = models.AutoField(primary_key = True)
    title = models.CharField('Titulo de la Portada', max_length = 100, blank = False, null = False)
    subtitle = models.CharField('Subtitulo de la Portada', max_length = 100, blank = False, null = False)
    price = models.CharField('Precio del Título', max_length = 100, blank = True, null = True)
    button = models.CharField('Boton de la Portada', max_length = 20, blank = False, null = False, default = "Compre Ahora")
    image = models.ImageField('Imagen de Presentación', upload_to='portadas', blank = True, null = True)
    priority = models.IntegerField('Orden de Prioridades', blank = False, null = False, default = 5)
    link = models.URLField('Enlace', blank = True, null = True)
    visibility = models.BooleanField('Activo/Inactivo', default = True)
    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)
    
    class Meta:
        verbose_name = 'Portada'
        verbose_name_plural = 'Portadas'
        ordering = ['priority', 'date_created']

    def __str__(self):
        return self.title

class Category(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField('Nombre de la Categoria', max_length = 100, blank = False, null = False)
    image = models.ImageField('Imagen de Presentación', upload_to='categorias', blank = True, null = True)
    priority = models.IntegerField('Orden de Prioridades', blank = False, null = False, default = 5)
    price = models.CharField('Precio', max_length = 100, blank = False, null = False, default = "20.000")
    date_created = models.DateTimeField(auto_now_add = True)
    slug = models.SlugField(blank = True, null = True)
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ["priority"]
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre)
        super(Category, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    
class Item(models.Model):
    id = models.AutoField(primary_key = True)
    title = models.CharField('Titulo del Producto', max_length = 100, blank = False, null = False)
    description = models.TextField('Descripcion del Producto', blank = True, null = True)
    image = models.ImageField('Imagen de Presentación', upload_to='productos', blank = True, null = True)
    price = models.IntegerField('Precio', blank = False, null = False)
    price_offer = models.IntegerField('Precio Oferta', blank = False, null = False, default=0 )
    priority = models.IntegerField('Orden de Prioridades', blank = False, null = False, default = 5)
    offer = models.BooleanField('En Oferta/Precio Normal', default = False)
    categories = models.ManyToManyField(Category, related_name='get_categoria')
    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)
    visibility = models.BooleanField('Activo/Inactivo', default = True)
    slug = models.SlugField(max_length = 100, blank = True, null = True)
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['priority', 'date_created']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Item, self).save(*args, **kwargs)

    def get_price(self):
        if self.offer:
            return self.price
        else:
            return self.price_offer

    def __str__(self):
        return self.title

    def get_images(self):
        return ItemImagen.objects.filter(item = self)

    def get_image(self):
        return ItemImagen.objects.filter(item = self).first()

class ItemImagen(models.Model):
    item = models.ForeignKey(Item, default = None, on_delete = models.CASCADE)
    imagen = models.ImageField(upload_to='productos/')

class ItemDetalle(models.Model):
    id = models.AutoField(primary_key = True)
    item = models.ForeignKey(Item, default = None, on_delete = models.CASCADE)
    model = models.CharField('Modelo', max_length = 100, blank = False, null = False, default = "")
    sizy = models.CharField('Talle', max_length = 100, blank = False, null = False, default = "")
    quantity = models.IntegerField('Cantidad', blank = False, null = False, default = 0)
    
    class Meta:
        verbose_name = 'Detalle'
        verbose_name_plural = 'Detalles'
        ordering = ["id"]


    
    
    

