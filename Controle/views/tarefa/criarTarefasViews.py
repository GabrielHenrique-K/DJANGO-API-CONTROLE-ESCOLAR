from rest_framework import generics
from Controle.models.Tarefa import Tarefa
from Controle.serializers.TarefaSerializer import  TarefaSerializer



class CriarTarefa(generics.CreateAPIView):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer