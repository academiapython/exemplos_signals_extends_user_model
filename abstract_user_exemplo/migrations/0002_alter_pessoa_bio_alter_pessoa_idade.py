# Generated by Django 4.1 on 2022-08-12 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abstract_user_exemplo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='bio',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='idade',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]