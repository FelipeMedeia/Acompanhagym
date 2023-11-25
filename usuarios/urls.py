from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('home/', views.home, name='homepage'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', views.login, name='login'),
    path('', views.index, name='index'),
    path('cadastro_cliente/', views.cadastro_cliente, name='cadastro_cliente'),
    path('dados_cliente/', views.dados_cliente, name='dados_cliente'),
    path('dados_detalhe/<int:id>/', views.dados_detalhe, name='dados_detalhe'),
    path('login_cliente/', views.login_cliente, name='login_cliente'),
    path('home_cliente/', views.home_cliente, name='home_cliente'),

    path('atividades/', views.exercicios, name='atividades'),
    path('excluir/<int:id>/', views.excluir_cliente, name='exluir'),
    path('excluir_exercicio/<int:id>/', views.excluir_exercicio, name='excluir_exercicio'),
]