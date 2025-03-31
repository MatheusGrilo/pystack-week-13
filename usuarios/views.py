from django.contrib import auth, messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.shortcuts import redirect, render


def cadastro(request):
    if request.method == "GET":
        return render(request, "cadastro.html")
    else:
        username = request.POST.get("username")
        senha = request.POST.get("senha")
        confirmar_senha = request.POST.get("confirmar_senha")

        if not senha == confirmar_senha:
            messages.add_message(
                request=request,
                level=constants.ERROR,
                message="As senhas devem ser iguais.",
            )
            return redirect("/usuarios/cadastro")

        if len(senha) < 6:
            messages.add_message(
                request=request,
                level=constants.ERROR,
                message="A senha deve ter no mínimo 6 caracteres.",
            )
            return redirect("/usuarios/cadastro")

        users = User.objects.filter(username=username)

        if users.exists():
            messages.add_message(
                request=request,
                level=constants.ERROR,
                message="Esse usuário já existe.",
            )
            return redirect("/usuarios/cadastro")

        User.objects.create_user(username=username, password=senha)

        return redirect("/usuarios/login")


def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        username = request.POST.get("username")
        senha = request.POST.get("senha")

        user = authenticate(request, username=username, password=senha)

        if user:
            auth.login(request, user)
            return redirect("/mentorados/")

        messages.add_message(request, constants.ERROR, "Username ou senha inválidos")
        return redirect("login")
