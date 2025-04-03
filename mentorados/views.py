from django.contrib import messages
from django.contrib.messages import constants
from django.shortcuts import redirect, render

from .models import Mentorados, Navigators


def mentorados(request):
    if not request.user.is_authenticated:
        return redirect("login")
    if request.method == "GET":
        mentorados = Mentorados.objects.filter(user=request.user)
        navigators = Navigators.objects.filter(user=request.user)

        estagios_flat = [i[1] for i in Mentorados.estagio_choices]
        qtd_estagios = []

        for i, j in Mentorados.estagio_choices:
            item = (
                Mentorados.objects.filter(estagio=i).filter(user=request.user).count()
            )
            qtd_estagios.append(item)

        print(estagios_flat)
        print(qtd_estagios)

        return render(
            request,
            "mentorados.html",
            {
                "estagios": Mentorados.estagio_choices,
                "navigators": navigators,
                "mentorados": mentorados,
                "estagios_flat": estagios_flat,
                "qtd_estagios": qtd_estagios,
            },
        )
    elif request.method == "POST":
        nome = request.POST.get("nome")
        foto = request.FILES.get("foto")
        estagio = request.POST.get("estagio")
        navigator = request.POST.get("navigator")

        mentorado = Mentorados(
            nome=nome,
            foto=foto,
            estagio=estagio,
            navigator_id=navigator,
            user=request.user,
        )

        mentorado.save()

        messages.add_message(
            request, constants.SUCCESS, "Mentorado cadastrado com sucesso."
        )
        return redirect("mentorados")
