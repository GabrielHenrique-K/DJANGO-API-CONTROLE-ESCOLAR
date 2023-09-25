from django.db import models

class Disciplina(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField()

    def __str__(self):
        return self.nome
