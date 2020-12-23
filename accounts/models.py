from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.dispatch import receiver
from django.db.models.signals import post_save
from .managers import CustomUserManager
from django.conf import settings


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    spouse_name = models.CharField(blank=True, max_length=100)
    date_of_birth = models.DateField(blank=True, null=True)
    

    def __str__(self):
        return self.email

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    avatar = models.ImageField(upload_to = 'avatares', null = True, blank = True)
    nombre = models.TextField('Nombre', max_length= 100, null = True, blank = True)
    apellido = models.TextField('Apellido', max_length= 100, null = True, blank = True)
    celular = models.TextField('Celular:', max_length= 10, null = True, blank = True)
    
    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
        ordering = ['-user']
    
    def __str__(self):
        return "{}, {}".format(self.nombre, self.apellido)

@receiver(post_save, sender=CustomUser)
def ensure_profile_exists(sender, instance, **kwargs):
    if kwargs.get('created', False):
        Profile.objects.get_or_create(user=instance)
        print("Se acaba de crear un usuario y su perfil enlazado")

