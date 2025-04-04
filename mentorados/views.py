import locale
from datetime import datetime, timedelta

from django.contrib import messages
from django.contrib.messages import constants
from django.shortcuts import redirect, render

from mentorados.auth import valida_token

from .models import DisponibilidadeHorarios, Mentorados, Navigators, Reuniao


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


def reunioes(request):
    if request.method == "GET":
        reunioes = Reuniao.objects.filter(data__mentor=request.user)

        return render(request, "reunioes.html", {"reunioes": reunioes})
    else:
        data = request.POST.get("data")

        data = datetime.strptime(data, "%Y-%m-%dT%H:%M")

        disponibilidade = DisponibilidadeHorarios.objects.filter(
            mentor=request.user
        ).filter(
            data_inicial__gte=(data - timedelta(minutes=50)),
            data_inicial__lte=(data + timedelta(minutes=50)),
        )

        if disponibilidade.exists():
            messages.add_message(
                request, constants.ERROR, "Você já possui uma reunião em aberto."
            )
            return redirect("reunioes")

        disponibilidade = DisponibilidadeHorarios(
            data_inicial=data, mentor=request.user
        )
        disponibilidade.save()

        messages.add_message(
            request, constants.SUCCESS, "Horário disponibilizado com sucesso."
        )
        return redirect("reunioes")


def auth(request):
    if request.method == "GET":
        return render(request, "auth_mentorado.html")
    else:
        token = request.POST.get("token")

        if not Mentorados.objects.filter(token=token).exists():
            messages.add_message(request, constants.ERROR, "Token inválido")
            return redirect("auth_mentorado")

        response = redirect("escolher_dia")
        response.set_cookie("auth_token", token, max_age=3600)
        return response


def escolher_dia(request):
    if not valida_token(request.COOKIES.get("auth_token")):
        return redirect("auth_mentorado")
    if request.method == "GET":
        disponibilidades = DisponibilidadeHorarios.objects.filter(
            data_inicial__gte=datetime.now(), agendado=False
        ).values_list("data_inicial", flat=True)
        locale.setlocale(locale.LC_TIME, "pt_BR.UTF-8")
        datas = []
        seen_dates = set()
        for i in disponibilidades:
            formatted_date = i.date().strftime("%d-%m-%Y")
            if formatted_date not in seen_dates:
                seen_dates.add(formatted_date)
                data_formatada = {
                    "data": formatted_date,
                    "mes": i.strftime("%B").capitalize(),
                    "dia_da_semana": i.strftime("%A").capitalize(),
                }
                datas.append(data_formatada)

        return render(request, "escolher_dia.html", {"datas": datas})


def agendar_reuniao(request):
    if not valida_token(request.COOKIES.get("auth_token")):
        return redirect("auth_mentorado")

    mentorado = valida_token(request.COOKIES.get("auth_token"))

    # TODO: Verificar se o horário agendado é realmente do mentor do mentorado

    if request.method == "GET":
        data = request.GET.get("data")
        data = datetime.strptime(data, "%d-%m-%Y")
        horarios = DisponibilidadeHorarios.objects.filter(
            data_inicial__gte=data,
            data_inicial__lt=data + timedelta(days=1),
            agendado=False,
            mentor=mentorado.user,
        )
        return render(
            request,
            "agendar_reuniao.html",
            {
                "horarios": horarios,
                "tags": Reuniao.tag_choices,
                "data": data.date(),
            },
        )
    else:
        # TODO: Atomicidade, implementar o A do ACID
        horario_id = request.POST.get("horario")
        tag = request.POST.get("tag")
        descricao = request.POST.get("descricao")

        reuniao = Reuniao(
            data_id=horario_id,
            mentorado=mentorado,
            tag=tag,
            descricao=descricao,
        )

        reuniao.save()

        horario = DisponibilidadeHorarios.objects.get(id=horario_id)
        horario.agendado = True
        horario.save()

        messages.add_message(
            request, constants.SUCCESS, "Reunião agendada com sucesso."
        )
        return redirect("escolher_dia")
