from rest_framework.views import APIView
from rest_framework.response import Response
from Controle.models.Tarefa import Tarefa
from Controle.serializers.TarefaSerializer import TarefaSerializer

class ListarTarefasAluno(APIView):
    """
    Classe de visualização para listar as tarefas de um aluno.
    """
    
    serializer_class = TarefaSerializer

    def get(self, request, aluno_id, format=None):
        # Obtém todas as tarefas associadas a um aluno específico pelo ID do aluno
        tarefas = Tarefa.objects.filter(aluno_id=aluno_id)
        
        # Serializa a lista de tarefas para a resposta
        serializer = TarefaSerializer(tarefas, many=True)
        
        # Retorna a lista de tarefas serializadas
        return Response(serializer.data)
