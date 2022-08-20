from django.db import models
from django.db.models.signals import post_save
from . apps import OneToOneExemploConfig

from django.dispatch import receiver
from abstract_user_exemplo.models import Pessoa

class Perfil(models.Model):
    user = models.OneToOneField(Pessoa, on_delete=models.CASCADE)
    dt_aniversario = models.DateField(null=True, blank=True)


@receiver(post_save, sender=Pessoa, dispatch_uid="id_post_save_pessoa")
def minha_funcao_callback(sender, **kwargs):
    print("Um novo registro foi inserido na tabela Pessoa")

    instance = kwargs.get('instance')
    if instance.idade < 18:
        OneToOneExemploConfig.menor_idade_signal.send(sender=Pessoa)

@receiver(OneToOneExemploConfig.menor_idade_signal, sender=Pessoa)
def cadastrou_menor_idade(sender, **kwargs):
    print('Interceptando ou recebendo informação de cadastro de menores de idade.')
