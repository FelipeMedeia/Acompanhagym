from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login as login_imp, authenticate
from .models import Clientes
from .models import Clientes, Exercicios


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


@login_required(login_url='../login/')
def dados_detalhe(request, id):
    exercicio = Exercicios.objects.filter(cliente=id)
    print('dd-d')
    print(exercicio)
    if exercicio:

        return render(request, 'exercicios.html', {'exercicio': exercicio})

    return render(request, 'dados_cliente.html', {'exercicio': exercicio})


@login_required(login_url='/login/')
def dados_cliente(request):
    if request.method == 'GET':
        print('if, dd-c')
        return render(request, 'dados_cliente.html')

    else:
        print('dados-else')
        braco = request.POST.get('braco')
        print(braco)
        perna = request.POST.get('perna')
        print(perna)
        peito = request.POST.get('peito')
        print(peito)
        costa = request.POST.get('costa')
        print(costa)
        gluteo = request.POST.get('gluteo')
        print(gluteo)
        cliente = Exercicios.objects.get(cliente=request.POST['identificador'])
        print('dd-c-e', cliente)

        exer = Exercicios.objects.create(braco=braco, perna=perna,
                                         peito=peito, costa=costa,
                                         gluteo=gluteo, cliente=cliente)
        exer.save()
    return redirect('/home')


@login_required(login_url='../login/')
def exercicios(request, id):
    exercicio = Exercicios.objects.filter(id=id)
    return render(request, 'exercicios.html', {'exercicio': exercicio})
@login_required(login_url='../login/')
def excluir_cliente(request, id):
    cliente = Clientes.objects.get(id=id)
    cliente.delete()
    return redirect('/home')
@login_required(login_url='../login/')
def excluir_exercicio(request, id):
    exercicio = Exercicios.objects.get(id=id)
    exercicio.delete()
    return redirect('/home')


def home_cliente(request):
    if request.method == 'GET':
        if len(request.session._session) == 0:
            return redirect('/login_cliente')
        else:
            nome = request.session['nome']
            id = request.session['id']
            exercicio = Exercicios.objects.filter(cliente=id)
            context = {
                'nome': nome
            }
            return render(request, 'home_cliente.html', {'exercicio': exercicio})


def login_cliente(request):
    if request.method == 'GET':
        return render(request, 'login_cliente.html')

    else:
        clientes = Clientes.objects.get(nome=request.POST['nome'])
        if clientes.email == request.POST['email']:
            request.session['nome'] = clientes.nome
            nome = request.session['nome']
            context = {
                'nome': nome
            }
            return redirect('/home_cliente')
        else:
            messages.error(request, ' Nome ou senha inválido! '
                                    'Por favor, tente novamente.')
    return redirect('/login_cliente')
