from rest_framework import generics
from Controle.models.Tarefa import  Tarefa
from Controle.serializers.TarefaSerializer import TarefaSerializer



class ListarTarefas(generics.ListAPIView):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer



#from rest_framework.views import APIView
#from rest_framework.response import Response
#from Controle.models.Tarefa import Tarefa
#from Controle.serializers.TarefaSerializer import TarefaSerializer
#
#class ListarTarefas(APIView):
#    def get(self, request, format=None):
#        tarefas = Tarefa.objects.all()
#        serializer = TarefaSerializer(tarefas, many=True)
#        return Response(serializer.data)
#


    #Quando um pedido HTTP GET é feito para esta API, o código recupera todas as tarefas do banco de dados usando Tarefa.objects.all(), em seguida, serializa essas tarefas usando um "TarefaSerializer" com a opção many=True, indicando que estamos lidando com uma lista de objetos.