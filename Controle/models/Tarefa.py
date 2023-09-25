from django.db import models
from Controle.models.Alunos import User
from Controle.models.Disciplina import Disciplina

class Tarefa(models.Model):
    # Título da tarefa
    titulo = models.CharField(max_length=200)

    # Descrição da tarefa
    descricao = models.TextField()

    # Data de entrega da tarefa
    data_entrega = models.DateField()

    # Aluno associado à tarefa
    aluno = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Task')

    # Disciplinas associadas à tarefa
    disciplinas = models.ManyToManyField(Disciplina, related_name='Task')

    def __str__(self):
        return self.titulo
