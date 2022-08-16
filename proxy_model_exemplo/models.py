from django.db import models

# Create your models here.
from abstract_user_exemplo.models import Pessoa
from . managers import PessoaProxyManager

class Aluno(Pessoa):
    manager = models.Manager()
    proxy_manager = PessoaProxyManager()

    class Meta:
        proxy = True

    def ola(self):
        return "Sou aluno da academia python"