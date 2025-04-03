from datetime import timedelta

from django.contrib.auth.models import User
from django.db import models


class Navigators(models.Model):
    nome = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Navigator"

    def __str__(self):
        return self.nome


class Mentorados(models.Model):
    estagio_choices = (("E1", "10-100k"), ("E2", "100-1KK"))
    nome = models.CharField(max_length=255)
    foto = models.ImageField(upload_to="fotos", null=True, blank=True)
    estagio = models.CharField(max_length=2, choices=estagio_choices)
    navigator = models.ForeignKey(
        Navigators, null=True, blank=True, on_delete=models.SET_NULL
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    criado_em = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Mentorado"

    def __str__(self):
        return self.nome


class DisponibilidadeHorarios(models.Model):
    data_inicial = models.DateTimeField(null=True, blank=True)
    mentor = models.ForeignKey(User, on_delete=models.CASCADE)
    agendado = models.BooleanField(default=False)

    @property
    def data_final(self):
        return self.data_inicial + timedelta(minutes=50)


class Reuniao(models.Model):
    tag_choices = (
        ("G", "Gestão"),
        ("M", "Marketing"),
        ("RH", "Gestão de pessoas"),
        ("I", "Impostos"),
    )

    data = models.ForeignKey(DisponibilidadeHorarios, on_delete=models.CASCADE)
    mentorado = models.ForeignKey(Mentorados, on_delete=models.CASCADE)
    tag = models.CharField(max_length=2, choices=tag_choices)
    descricao = models.TextField()
