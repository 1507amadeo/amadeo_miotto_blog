from django.urls import path

from home import views

app_name='home'
urlpatterns = [
    path('', views.main, name='main'),
    path('pagina_error', views.pagina_error, name='pagina-error'),
    path('about_us', views.about_us, name='about-us'),
]