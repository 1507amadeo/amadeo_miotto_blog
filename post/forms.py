from django import forms
from post.models import PostImagen

class ImagenForm(forms.ModelForm):
    class Meta:
        model = PostImagen
        fields = ('image', )