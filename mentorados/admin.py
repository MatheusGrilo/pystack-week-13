from django.contrib import admin

from .models import DisponibilidadeHorarios, Mentorados, Navigators

admin.site.register(Navigators)
admin.site.register(Mentorados)
admin.site.register(DisponibilidadeHorarios)
# Register your models here.
