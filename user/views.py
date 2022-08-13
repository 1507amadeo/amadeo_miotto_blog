from msilib.schema import ListView
import os
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from post.models import Post
from user.forms import UserRegisterForm, UserEditForm, AvatarForm
from user.models import Avatar, User
from django.contrib import messages
from django.forms import model_to_dict
from django.views.generic.detail import DetailView



# Create your views here.
def register(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuario creado exitosamente!")
            return redirect("user:user-login")
        else: messages.error(request,"Datos Inválidos")
    form = UserRegisterForm()
    
    return render(
        request=request,
        context={"form":form},
        template_name="user/register.html",
    )


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home:main")

        return render(
            request=request,
            context={'form': form},
            template_name="user/login.html",
        )

    form = AuthenticationForm()
    return render(
        request=request,
        context={'form': form},
        template_name="user/login.html",
    )


def logout_request(request):
    logout(request)
    return redirect("user:user-login")

@login_required
def user_update(request):
    user = request.user
    if request.method == 'POST':
        form = UserEditForm(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            user.first_name = informacion['first_name']
            user.last_name = informacion['last_name']
            user.email = informacion['email']
            user.password1 = informacion['password1']
            user.password2 = informacion['password2']
            user.perfil=informacion['profile']
            user.save()

            return redirect('home:main')

    form= UserEditForm(model_to_dict(user))
    return render(
        request=request,
        context={'form': form},
        template_name="user/user_form.html",
    )


@login_required
def avatar_load(request):
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid  and len(request.FILES) != 0:
            image = request.FILES['image']
            avatars = Avatar.objects.filter(user=request.user.id)
            if not avatars.exists():
                avatar = Avatar(user=request.user, image=image)
            else:
                avatar = avatars[0]
                if len(avatar.image) > 0:
                    os.remove(avatar.image.path)
                avatar.image = image
            avatar.save()
            messages.success(request, "Imagen cargada exitosamente")
            return redirect('home:main')
            

    form= AvatarForm()
    return render(
        request=request,
        context={"form": form},
        template_name="user/avatar_form.html",
    )
class AutorDetailView(DetailView):
    model=User
    template_name="user/autor_detail.html"
