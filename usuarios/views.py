from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login as login_imp


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


#@login_required(login_url='/cadastro/')
def home(request):
    return render(request, 'home.html')
