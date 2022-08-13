from django.urls import path
from comment import views

app_name='comment'
urlpatterns =[
    path('comentarios',views.comentarios, name='Comentarios'),
    path('comentario_formulario/<int:pk>', views.comentario_formulario , name='ComentarioFormulario'),
]