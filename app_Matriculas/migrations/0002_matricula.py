# Generated by Django 2.1 on 2022-05-28 22:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_Matriculas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=8)),
                ('tipo', models.CharField(choices=[('ORDINARIA', 'ORDINARIA'), ('EXTRAORDINARIA', 'EXTRAORDINARIA'), ('ESPECIAL', 'ESPACIAL')], default='available', max_length=45)),
                ('fecha', models.DateField()),
                ('curso', models.CharField(choices=[('I', 'I CICLO'), ('II', 'II CICLO'), ('III', 'III CICLO'), ('IV', 'IV CICLO'), ('V', 'V CICLO')], default='available', max_length=45)),
                ('carrera', models.CharField(max_length=100)),
                ('fk_alumno', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app_Matriculas.Alumno')),
            ],
        ),
    ]
