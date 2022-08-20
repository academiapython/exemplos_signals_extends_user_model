from django.apps import AppConfig
from django.dispatch import Signal

class OneToOneExemploConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'one_to_one_exemplo'
    menor_idade_signal = Signal()
