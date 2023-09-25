from django.db import models

class Disciplina(models.Model):
    # Nome da disciplina (único)
    nome = models.CharField(max_length=100, unique=True)

    # Descrição da disciplina
    descricao = models.TextField()

    def __str__(self):
        return self.nome
