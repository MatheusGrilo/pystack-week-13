# Generated by Django 5.1.7 on 2025-03-31 21:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mentorados', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mentorados',
            options={'verbose_name': 'Mentorado'},
        ),
        migrations.AlterModelOptions(
            name='navigators',
            options={'verbose_name': 'Navigator'},
        ),
    ]
