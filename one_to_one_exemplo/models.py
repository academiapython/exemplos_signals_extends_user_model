from django.db import models
from django.db.models.signals import post_save

from django.dispatch import receiver
from abstract_user_exemplo.models import Pessoa


class Perfil(models.Model):
    user = models.OneToOneField(Pessoa, on_delete=models.CASCADE)
    dt_aniversario = models.DateField(null=True, blank=True)


@receiver(post_save, sender=Pessoa, dispatch_uid="id_post_save_pessoa")
def minha_funcao_callback(sender, **kwargs):
    print("Um novo registro foi inserido na tabela Pessoa")