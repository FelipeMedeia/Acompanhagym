from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login as login_imp, authenticate
from .models import Clientes
from datetime import date


# Create your views here.
def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro1.html')
    else:
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        if len(senha) <= 5:
            messages.error(request, 'Senha deve conter no minimo 6 caracteres!')
            return redirect('cadastro')

        else:
            user = User.objects.filter(email=email).first()

            if user:
                messages.error(request, 'Já existe um usuário cadastrado com esse email!!')
                return redirect('cadastro')

            else:
                user = User.objects.create_user(username=nome, first_name=nome, email=email, password=senha)
                user.save()
                if user:
                    login_imp(request, user)
                    return redirect('/home', user.first_name)


@login_required(login_url='/login/')
def home(request):
    cliente = Clientes.objects.filter(user=request.user, active=True)
    return render(request, 'home.html', {'cliente': cliente})


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')

        user = authenticate(username=nome, password=senha)
        if user:
            login_imp(request, user)
            return redirect('/home')
        else:
            messages.error(request, ' Nome ou senha inválido! '
                                    'Por favor, tente novamente.')
    return redirect('/login')


def index(request):
    return render(request, 'index.html')


@login_required(login_url='/login/')
def cadastro_cliente(request):
    if request.method == "GET":
        return render(request, 'cadastro_cliente.html')
    else:
        nome = request.POST.get('nome')
        endereco = request.POST.get('endereco')
        data_nascimento = request.POST.get('data_nascimento')
        email = request.POST.get('email')
        peso = request.POST.get('peso')
        altura = request.POST.get('altura')
        user = request.user

        cliente = Clientes.objects.filter(email=email).first()
        if cliente:
            messages.error(request, 'Já existe um cliente cadastrado com esse Email!!')
            return render('cadastro_cliente.html')

        else:
            cliente = Clientes.objects.create(nome=nome, email=email, data_nascimento=data_nascimento,
                                              endereco=endereco, peso=peso, altura=altura, user=user)
            cliente.save()

    return redirect('/home')


@login_required(login_url='/login/')
def dados_cliente(request):
    if request.method == 'GET':
        return render(request, 'dados_cliente.html')

    else:
        braco = request.POST.get('braco')
        perna = request.POST.get('perna')
        peito = request.POST.get('peito')
        costa = request.POST.get('costa')
        gluteo = request.POST.get('gluteo')

        exer = Clientes.clientes_exercicios(braco=braco, perna=perna,
                                            peito=peito, costa=costa,
                                            gluteo=gluteo)
        exer.save()

