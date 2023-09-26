from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('home/', views.home, name='homepage'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    #path('login/', views.login, name='login'),

]