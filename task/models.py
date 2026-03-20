from django.db import models

class Tarefa(models.Model):

    titulo = models.CharField(
        max_length=30,
        null=False,
        blank=False,
    )

    desc = models.CharField(
        max_length=255,
        null=False,
        blank=False,
    )

    data_vencimento = models.DateField(
        
    )

    status = models.BooleanField(
   
    )