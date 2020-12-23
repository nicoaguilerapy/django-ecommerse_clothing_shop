from django.db import models
from django.utils.text import slugify


class Modelo(models.Model):
    id = models.AutoField(primary_key = True)
    Modelo = models.CharField('Talle', max_length = 100, blank = False, null = False)
    
    class Meta:
        verbose_name = 'Talle'
        verbose_name_plural = 'Talles'
        ordering = ["id"]
    
    def __str__(self):
        return self.talle

class Categoria(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre de la Categoria', max_length = 100, blank = False, null = False)
    imagen_principal = models.ImageField('Imagen de Presentación', upload_to='categorias', blank = True, null = True)
    orden = models.IntegerField('Orden de Prioridades', blank = False, null = False, default = 5)
    fecha_creacion = models.DateTimeField(auto_now_add = True)
    slug = models.SlugField(blank = True, null = True)
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ["orden"]
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre)
        super(Categoria, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    id = models.AutoField(primary_key = True)
    titulo = models.CharField('Titulo del Producto', max_length = 100, blank = False, null = False)
    descripcion = models.TextField('Descripcion del Producto', blank = True, null = True)
    precio = models.IntegerField('Precio', blank = False, null = False)
    precio_oferta = models.IntegerField('Precio Oferta', blank = False, null = False, default=0 )
    imagen = models.ImageField('Imagén', blank = True)
    orden = models.IntegerField('Orden de Prioridades', blank = False, null = False, default = 5)
    oferta = models.BooleanField('En Oferta/Precio Normal', default = False)
    categorias = models.ManyToManyField(Categoria, related_name='get_categoria')
    talles = models.CharField('Talles', max_length = 255, blank = True, null = True, default = 'Talles entre comas')
    modelos = models.CharField('Modelos', max_length = 255, blank = True, null = True, default = 'Modelos entre comas')
    fecha_creacion = models.DateTimeField(auto_now_add = True)
    fecha_modificacion = models.DateTimeField(auto_now = True)
    estado = models.BooleanField('Activo/Inactivo', default = True)
    slug = models.SlugField(max_length = 100, blank = True, null = True)
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['orden', 'fecha_creacion']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titulo)
        super(Producto, self).save(*args, **kwargs)

    def __str__(self):
        return self.titulo

class ProductoImagen(models.Model):
    producto = models.ForeignKey(Producto, default = None, on_delete = models.CASCADE)
    imagen = models.ImageField(upload_to='productos/')

    def __str__(self):
        return self.producto.titulo

class Portada(models.Model):
    id = models.AutoField(primary_key = True)
    titulo = models.CharField('Titulo de la Portada', max_length = 100, blank = False, null = False)
    subtitulo = models.CharField('Subtitulo de la Portada', max_length = 100, blank = False, null = False)
    boton = models.CharField('Boton de la Portada', max_length = 20, blank = False, null = False, default = "Compre Ahora")
    imagen_principal = models.ImageField('Imagen de Presentación', upload_to='portadas', blank = True, null = True)
    orden = models.IntegerField('Orden de Prioridades', blank = False, null = False, default = 5)
    categoria = models.OneToOneField(Categoria, on_delete = models.DO_NOTHING)
    estado = models.BooleanField('Activo/Inactivo', default = True)
    fecha_creacion = models.DateTimeField(auto_now_add = True)
    fecha_modificacion = models.DateTimeField(auto_now = True)
    
    class Meta:
        verbose_name = 'Portada'
        verbose_name_plural = 'Portadas'
        ordering = ['orden', 'fecha_creacion']

    def __str__(self):
        return self.titulo
    
    

    
    
    

