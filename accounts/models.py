from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    avatar = models.ImageField(upload_to = 'avatares', null = True, blank = True)
    nombre = models.TextField('Nombre', max_length= 100, null = True, blank = True)
    apellido = models.TextField('Apellido', max_length= 100, null = True, blank = True)
    celular = models.TextField('Celular', max_length= 10, null = True, blank = True)
    
    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
        ordering = ['-user']
    
    def __str__(self):
        return "{}, {}".format(self.nombre, self.apellido)



