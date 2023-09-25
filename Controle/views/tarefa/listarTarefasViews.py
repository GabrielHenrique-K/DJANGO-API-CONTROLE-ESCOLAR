from rest_framework.views import APIView
from rest_framework.response import Response
from Controle.models.Tarefa import Tarefa
from Controle.serializers.TarefaSerializer import TarefaSerializer

class ListarTarefas(APIView):
    """
    Classe de visualização para listar todas as tarefas.
    """

    def get(self, request, format=None):
        # Obtém todas as tarefas do banco de dados
        tarefas = Tarefa.objects.all()

        # Serializa a lista de tarefas para a resposta
        serializer = TarefaSerializer(tarefas, many=True)

        # Retorna a lista de tarefas serializadas
        return Response(serializer.data)
