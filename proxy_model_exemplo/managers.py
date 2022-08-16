from django.db import models

class PessoaProxyManager(models.Manager):
    def qtde_id_maior_tres(self):
        return self.filter(id__gt=3)

    def get_queryset(self):
        return super().get_queryset().filter(id__lt=4)
