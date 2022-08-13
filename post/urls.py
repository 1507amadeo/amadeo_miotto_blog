from django.urls import path
from post import views

app_name='post'
urlpatterns =[
    path('post', views.PostListView.as_view(), name='post-list'),
    path('post/add/', views.PostCreateView.as_view(), name='post-add'),
    path('post/<int:pk>/detail', views.PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', views.PostDeleteView.as_view(), name='post-delete'),
    path('post_search', views.post_search, name='post-search'),
    path('imagen/<int:pk>/load', views.imagen_load, name='imagen-load'),
    
]