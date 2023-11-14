# Generated by Django 4.2.5 on 2023-11-13 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('hora_inicio', models.TimeField()),
                ('hora_fin', models.TimeField()),
                ('fecha', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=50, verbose_name='Apellido')),
                ('mail', models.EmailField(max_length=150, verbose_name='Email')),
            ],
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150, verbose_name='Nombre')),
                ('miembros', models.ManyToManyField(related_name='grupos', to='core.persona')),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('descripcion', models.TextField(verbose_name='Descripcion')),
                ('inicio', models.DateTimeField(verbose_name='Inicio')),
                ('fin', models.DateTimeField(verbose_name='Fin')),
                ('organizador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.persona')),
                ('participantes', models.ManyToManyField(to='core.grupo')),
            ],
        ),
    ]
