from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.dispatch import receiver
from django.db.models.signals import post_save
from .managers import CustomUserManager
from django.conf import settings
from itertools import chain
from datetime import datetime
from datetime import timedelta


LABEL_CHOICES = (
    ('PY01', 'Concepcion'),
    ('PY02', 'San Pedro'),
    ('PY03', 'Cordillera'),
    ('PY04', 'Guaira'),
    ('PY05', 'Caaguazu'),
    ('PY06', 'Caazapa'),
    ('PY07', 'Itapua'),
    ('PY08', 'Misiones'),
    ('PY09', 'Paraguari'),
    ('PY10', 'Alto Parana'),
    ('PY11', 'Central'),
    ('PY12', 'Neembucu'),
    ('PY13', 'Amambay'),
    ('PY14', 'Canindeyu'),
    ('PY15', 'Presidente Hayes'),
    ('PY16', 'Boqueron'),
    ('PY17', 'Alto Paraguay'),
)


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
    image = models.ImageField(upload_to = 'profile', null = True, blank = True)
    document = models.IntegerField('Documento', blank = True, null = True)
    first_name = models.CharField('Nombres', max_length = 200, blank = True, null = True)
    last_name = models.CharField('Apellidos', max_length = 220, blank = True, null = True)
    region = models.CharField('Departamento', choices=LABEL_CHOICES, max_length=4)
    city = models.CharField('Ciudad', max_length = 220, blank = True, null = True)
    phone = models.TextField('Celular:', max_length= 10, null = True, blank = True)
    date_created = models.DateTimeField(auto_now_add = True, null=True, blank=True)
    
    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
        ordering = ['-document']
    
    def __str__(self):
        return "{}, {}".format(self.first_name, self.last_name)

@receiver(post_save, sender=CustomUser)
def ensure_profile_exists(sender, instance, **kwargs):
    if kwargs.get('created', False):
        Profile.objects.get_or_create(user=instance)
        print("Se acaba de crear un usuario y su perfil enlazado")

