from django.contrib import admin

from .models import DisponibilidadeHorarios, Mentorados, Navigators, Reuniao

admin.site.register(Navigators)
admin.site.register(Mentorados)
admin.site.register(DisponibilidadeHorarios)
admin.site.register(Reuniao)
# Register your models here.
