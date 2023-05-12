# Generated by Django 4.2.1 on 2023-05-12 02:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cohorteTimer', '0003_profesorcohorte'),
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('update_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('position', models.CharField(choices=[('F', 'Formador'), ('CF', 'Coformador')], default='F', max_length=2)),
            ],
        ),
        migrations.RemoveField(
            model_name='profesorcohorte',
            name='id_cohorte',
        ),
        migrations.RemoveField(
            model_name='profesorcohorte',
            name='id_profesor',
        ),
        migrations.DeleteModel(
            name='Cohorte',
        ),
        migrations.DeleteModel(
            name='Profesor',
        ),
        migrations.DeleteModel(
            name='ProfesorCohorte',
        ),
        migrations.DeleteModel(
            name='Programa',
        ),
    ]