from cgitb import enable
from datetime import datetime
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.

class Post(models.Model):
    title=models.TextField(max_length=100)
    subtitle=models.TextField(max_length=80)
    texto= RichTextField()
    autor=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,null=True)  #-- preguntar
    fecha_publicacion=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'Titulo: {self.title} --- Autor: Nombre:{self.autor} --- Fecha de Publicación: {self.fecha_publicacion}'

    def get_absolute_url(self):
        """
        Devuelve el URL a una instancia particular
        """
        return reverse('post:post-detail', args=[str(self.id)])

class PostImagen(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='imagenes', null=True, blank=True)

    def __str__(self):
        return f'url: {self.image.url}'