from django.urls import path

from user import views


app_name='user'
urlpatterns = [
    path('login', views.login_request, name='user-login'),
    path('logout', views.logout_request, name='user-logout'),
    path('register', views.register, name='user-register'),
    path('register/update', views.user_update, name='user-update'),
    path('avatar/load', views.avatar_load, name='avatar-load'),
    path('user/<int:pk>/detail', views.AutorDetailView.as_view(), name='autor-detail'),
]