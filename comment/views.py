from django.shortcuts import render
from comment.models import Comentario
from comment.forms import ComentarioFormulario
from django.contrib.auth.decorators import login_required

from post.models import Post
from user.models import User

# Create your views here.
def comentarios(request):
    comentarios = Comentario.objects.all()

    context_dict = {
        'comentario_form': comentarios
    }

    return render(
        request=request,
        context=context_dict,
        template_name="comment/comentarios.html"
    )

@login_required
def comentario_formulario(request,pk):
    if request.method == 'POST':
        comentario_form = ComentarioFormulario(request.POST)
        if comentario_form.is_valid():
            post=Post.objects.get(id=pk)
            usuario= request.user
            data = comentario_form.cleaned_data
            mi_comentario = Comentario(descripcion=data['descripcion'],post=post, autor=usuario)
            mi_comentario.save()

            comentarios = Comentario.objects.all()
            context_dict = {
                'comentario_form': comentarios
            }
            return render(
                request=request,
                context=context_dict,
                template_name="comment/comentarios.html"
            )

    comentario_form = ComentarioFormulario(request.POST)
    context_dict = {
        'comentarios': comentario_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='comment/comentario_formulario.html'
    )
