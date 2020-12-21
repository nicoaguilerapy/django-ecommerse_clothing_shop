from django.db import models

class Social(models.Model):
    slug = models.SlugField(max_length = 100, blank = True, null = True)
    social = models.CharField('Nombre de la Red Social', max_length = 100)
    url= models.URLField('URL de la red Social', max_length = 100, blank = True, null = True)
    fecha_creacion = models.DateTimeField(auto_now_add = True)
    fecha_modificacion = models.DateTimeField(auto_now = True)
    
    class Meta:
        verbose_name = 'Red Social'
        verbose_name_plural = 'Redes Sociales'
        ordering = ['-social']
        
    def __str__(self):
        return self.social
    
class Fact(models.Model):
    slug = models.SlugField(max_length = 100, blank = True, null = True)
    fact = models.CharField('Tipo de Dato',max_length = 100, blank = False, null = False)
    value = models.CharField('Texto', max_length = 100, blank = False, null = False)
    fecha_creacion = models.DateTimeField(auto_now_add = True)
    fecha_modificacion = models.DateTimeField(auto_now = True)
    
    class Meta:
        verbose_name = 'Dato'
        verbose_name_plural = 'Datos'
        ordering = ['id']
        
    def __str__(self):
        cadena = self.fact +": "+self.value
        return cadena

class Number(models.Model):
    id = models.AutoField(primary_key = True)
    category = models.CharField('Categoria del Número', max_length = 100, blank = False, null = False)
    number = models.CharField('Número de Contacto', max_length = 12, blank = False, null = False)
    whatsapp = models.BooleanField('Tiene WhatsApp/No tiene', default = True)
    estado = models.BooleanField('Activo/Inactivo', default = True)
    fecha_creacion = models.DateTimeField(auto_now_add = True)
    fecha_modificacion = models.DateTimeField(auto_now = True)
    
    class Meta:
        verbose_name = 'Número'
        verbose_name_plural = 'Números'
        ordering = ['id']
        
    def __str__(self):
        return self.number
    
class Email(models.Model):
    id = models.AutoField(primary_key = True)
    category = models.CharField('Categoria del Email', max_length = 100, blank = False, null = False)
    email = models.EmailField('Dirección de Correo Electrónico', max_length = 100, blank = False, null = False)
    estado = models.BooleanField('Activo/Inactivo', default = True)
    fecha_creacion = models.DateTimeField(auto_now_add = True)
    fecha_modificacion = models.DateTimeField(auto_now = True)
    
    class Meta:
        verbose_name = 'Correo Electronico'
        verbose_name_plural = 'Correos Electronicos'
        ordering = ['id']
        
    def __str__(self):
        return self.email