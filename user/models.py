from datetime import datetime
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


# Create your models here.
class Avatar(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='avatars', null=True, blank=True)

    def __str__(self):
        return f'url: {self.image.url}'

class User(AbstractUser):
    fecha_nacimiento=models.DateField(default='1950-05-04')
    fecha_y_hora_creacion=models.DateTimeField(auto_now_add=True)
    tipo_perfil  = (
        ('E', 'Editor'),
        ('L', 'Lector'),
        ('A', 'Administrador'),
        )
    perfil=models.CharField(
        max_length=1,
        choices=tipo_perfil,
        blank=True,
        default='L',
        help_text='Perfil del Usuario')
    
    def get_absolute_url(self):
        return reverse('autor-detail', args=[str(self.id)])