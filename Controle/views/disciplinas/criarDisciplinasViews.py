from rest_framework.views import APIView
from rest_framework.response import Response
from Controle.models.Disciplina import Disciplina
from Controle.serializers.DisciplinaSerializer import DisciplinaSerializer
from rest_framework import status

class CriarDisciplina(APIView):
    """
    Classe de visualização para criar uma disciplina e atribuir uma descrição.
    """

    def post(self, request, format=None):
        # Cria uma instância do serializador DisciplinaSerializer com os dados da requisição
        serializer = DisciplinaSerializer(data=request.data)
        
        # Verifica se os dados são válidos de acordo com o serializador
        if serializer.is_valid():
            # Salva a disciplina no banco de dados
            serializer.save()
            
            # Retorna uma resposta de sucesso com os dados da disciplina criada
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        # Se os dados não forem válidos, retorna uma resposta de erro com os detalhes dos erros
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
