from django.shortcuts import render
from django.db.models import Q

from user.models import Avatar
from post.models import Post


def main(request):
    avatar_ctx = get_avatar_url_ctx(request)
    posts= Post.objects.all()
    context_dict = {**avatar_ctx, 'posts': posts}
    return render(
        request=request,
        context=context_dict,
        template_name="home/main.html"
    )

def get_avatar_url_ctx(request):
    avatars = Avatar.objects.filter(user=request.user.id)
    if avatars.exists():
        return {"url": avatars[0].image.url}
    return {}

def pagina_error(request):
    return render(
        request=request,
        template_name="home/pagina_error.html"
    )

def about_us(request):
    return render(
        request=request,
        template_name="home/about_us.html"
    )