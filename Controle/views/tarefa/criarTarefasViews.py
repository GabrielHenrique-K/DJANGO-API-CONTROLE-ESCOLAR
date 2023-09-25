from Controle.models.Alunos import User
from Controle.models.Tarefa import Tarefa
from Controle.serializers.TarefaSerializer import TarefaSerializer
from Controle.models.Disciplina import Disciplina
from rest_framework import serializers
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

class CriarTarefa(APIView):
    """
    Classe de visualização para criar uma tarefa.
    """
    
    def post(self, request):
        # Cria uma instância do serializador TarefaSerializer com os dados da requisição
        serializer = TarefaSerializer(data=request.data)
       
        # Verifica se os dados são válidos de acordo com o serializador
        if serializer.is_valid():
            # Salva a tarefa no banco de dados
            serializer.save()         
            
            # Retorna uma resposta de sucesso com os dados da tarefa criada
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        
        # Se os dados não forem válidos, retorna uma resposta de erro com os detalhes dos erros
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
