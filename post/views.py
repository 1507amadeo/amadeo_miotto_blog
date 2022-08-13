import os
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from post.forms import ImagenForm
from post.models import Post, PostImagen
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect

from user.models import User





# Create your views here.
class PostListView(ListView):
    model=Post
    template_name="post/post_list.html"

class PostDetailView(DetailView):
    model=Post
    template_name="post/post_detail.html"

class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post
    success_url: reverse_lazy('post:post-list')
    fields=['title','subtitle','texto','autor']

class PostDeleteView(LoginRequiredMixin,DeleteView):
    model=Post
    success_url='/'

class PostUpdateView(LoginRequiredMixin,UpdateView):
    model= Post
    success_url: reverse_lazy('post:post-list')
    fields=['title','subtitle','texto']

def post_search(request):
    context_dict = dict()
    if request.method == 'GET':
        if request.GET.get('autor_search') and request.GET.get('fecha_search'):
            search_param1 = request.GET.get('autor_search')
            search_param2 = request.GET.get('fecha_search')
            query = Q(autor__username__icontains=search_param1)
            query.add(Q(autor__first_name__icontains=search_param1), Q.OR)
            query.add(Q(autor__last_name__icontains=search_param1), Q.OR) 
            query.add(Q(autor__last_name__icontains=search_param1), Q.OR)
            query.add(Q(fecha_publicacion__contains=search_param2), Q.AND)
            posts = Post.objects.filter(query)
            context_dict = {
                'posts': posts
            }
        elif request.GET.get('autor_search') :
            search_param = request.GET.get('autor_search')           
            query = Q(autor__username__icontains=search_param)
            query.add(Q(autor__first_name__icontains=search_param), Q.OR)
            query.add(Q(autor__last_name__icontains=search_param), Q.OR) 
            posts = Post.objects.filter(query)
            context_dict = {
                'posts': posts
            }
        elif request.GET.get('fecha_search'):
            search_param = request.GET.get('fecha_search')
            posts = Post.objects.filter(fecha_publicacion__contains=search_param)
            context_dict = {
                'posts': posts
            }
    return render(
            request=request,
            context=context_dict,
            template_name="post/post_search.html",
        )

@login_required
def imagen_load(request,pk):
    if request.method == 'POST':
        form = ImagenForm(request.POST, request.FILES)
        if form.is_valid  and len(request.FILES) != 0:
            imagen = request.FILES['image']
            imagenes = PostImagen.objects.filter(post__id=pk)
            posts=Post.objects.get(id=pk)
            if not imagenes.exists():
                imagen = PostImagen(post=posts, image=imagen)
            else:
                imagen = imagenes[0]
                if len(imagen.image) > 0:
                    os.remove(imagen.image.path)
                imagen.image = imagen
            imagen.save()
            messages.success(request, "Imagen cargada exitosamente")
            return redirect('home:main')

    form= ImagenForm()
    return render(
        request=request,
        context={"form": form},
        template_name="post/post_imagen_form.html",
    )