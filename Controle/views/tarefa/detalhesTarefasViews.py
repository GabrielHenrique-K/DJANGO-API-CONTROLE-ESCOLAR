from rest_framework import generics
from Controle.models.Tarefa import Tarefa
from Controle.serializers.TarefaSerializer import TarefaSerializer




class DetalhesTarefa(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer
    lookup_field = 'id'