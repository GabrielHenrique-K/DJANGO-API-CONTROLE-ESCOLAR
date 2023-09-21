from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    
class TarefaDisciplina(models.Model):  
    nome = models.CharField(max_length=100)


class Tarefa(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    data_entrega = models.DateField()
    concluida = models.BooleanField(default=False)

    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE) 
    disciplinas = models.ManyToManyField(TarefaDisciplina) 

    def __str__(self):
        return self.titulo