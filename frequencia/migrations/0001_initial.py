# Generated by Django 5.1.6 on 2025-02-22 18:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('alunos', '0002_aluno_email_aluno_matricula'),
    ]

    operations = [
        migrations.CreateModel(
            name='Frequencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('presente', models.BooleanField(default=True)),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='frequencias', to='alunos.aluno')),
            ],
        ),
    ]
