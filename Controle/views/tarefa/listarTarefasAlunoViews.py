from rest_framework import generics
from Controle.models.Tarefa import  Tarefa
from Controle.serializers.TarefaSerializer import TarefaSerializer



class ListarTarefasAluno(generics.ListAPIView):
    serializer_class = TarefaSerializer

    def get_queryset(self):
        aluno_id = self.kwargs['aluno_id']
        return Tarefa.objects.filter(aluno_id=aluno_id)