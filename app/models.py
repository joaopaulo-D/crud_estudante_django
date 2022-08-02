from django.db import models
from django.urls import *

class Estudante(models.Model):
    nome = models.CharField(max_length=100, null=True)
    matricula = models.CharField(max_length=100, null=True)
    curso = models.CharField(max_length=100, null=True)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('estudante-edit', kwargs={'pk': self.pk})