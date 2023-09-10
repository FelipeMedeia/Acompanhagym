from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect


# Create your views here.


def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(username=nome).first()

        if user:
            User.unique_error_message()
            return redirect('cadastro')

        else:
            user = User.objects.create_user(username=nome, first_name=nome, email=email, password=senha)
            user.save()
            messages.success(request, 'Usuário cadastrado com sucesso!!')
            return redirect('cadastro')
