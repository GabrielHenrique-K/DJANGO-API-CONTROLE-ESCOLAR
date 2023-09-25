from django.db import models
from Controle.models.Alunos import User
from Controle.models.Disciplina import Disciplina


class Tarefa(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    data_entrega = models.DateField()

    aluno = models.ForeignKey(User, on_delete=models.CASCADE, related_name= 'Task')
    disciplinas = models.ManyToManyField(Disciplina, related_name='Task')

    def __str__(self):
        return self.titulo