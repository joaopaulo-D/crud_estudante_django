# Generated by Django 4.0.6 on 2022-08-02 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estudante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, null=True)),
                ('matricula', models.CharField(max_length=100, null=True)),
                ('curso', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]