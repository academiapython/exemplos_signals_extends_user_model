# Generated by Django 4.1 on 2022-08-12 22:23

import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('abstract_user_exemplo', '0002_alter_pessoa_bio_alter_pessoa_idade'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('abstract_user_exemplo.pessoa',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]