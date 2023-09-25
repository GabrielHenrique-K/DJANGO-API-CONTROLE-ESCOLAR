from rest_framework.views import APIView
from rest_framework.response import Response
from Controle.models.Tarefa import Tarefa
from Controle.serializers.TarefaSerializer import TarefaSerializer

class ListarTarefas(APIView):
   def get(self, request, format=None):
       tarefas = Tarefa.objects.all()
       serializer = TarefaSerializer(tarefas, many=True)
       return Response(serializer.data)



   