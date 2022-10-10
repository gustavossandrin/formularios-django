# Generated by Django 4.1.2 on 2022-10-09 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40)),
                ('data_nascimento', models.DateField(blank=True, null=True)),
                ('sexo', models.CharField(choices=[('m', 'Masculino'), ('f', 'Feminino'), ('n', 'Neutro')], max_length=1)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
    ]
