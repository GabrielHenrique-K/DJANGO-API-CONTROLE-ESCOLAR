from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from Controle.models.Alunos import User
from Controle.serializers.AlunosSerializer import AlunoSerializer

class CriarAluno(APIView):
    """
    Classe de visualização para criar um aluno com base em dois modelos.
    """
    
    def post(self, request, *args, **kwargs):
        # Cria uma instância do serializador AlunoSerializer com os dados da requisição
        serializer = AlunoSerializer(data=request.data)
        
        # Verifica se os dados são válidos de acordo com o serializador
        if serializer.is_valid():
            # Salva o aluno no banco de dados
            serializer.save()
            
            # Retorna uma resposta de sucesso com os dados do aluno criado
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        # Se os dados não forem válidos, retorna uma resposta de erro com os detalhes dos erros
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
