from rest_framework import generics
from Controle.models.Tarefa import Tarefa
from Controle.serializers.TarefaSerializer import  TarefaSerializer



class CriarTarefa(generics.CreateAPIView):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer



#from rest_framework.views import APIView
#from rest_framework.response import Response
#from Controle.models.Tarefa import Tarefa
#from Controle.serializers.TarefaSerializer import TarefaSerializer
#from rest_framework import status

#class CriarTarefa(APIView):
#    def post(self, request, format=None):
#        serializer = TarefaSerializer(data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status=status.HTTP_201_CREATED)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #"APIView" chamada "CriarTarefa" que é responsável por criar uma nova tarefa. Quando um pedido HTTP POST é feito para esta API com os detalhes da tarefa em formato JSON, o código verifica se os dados são válidos usando um "TarefaSerializer".
