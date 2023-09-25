from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from Controle.models.Alunos import User
from Controle.serializers.AlunosSerializer import AlunoSerializer
from django.http import Http404

class DetalhesAluno(APIView):
    """
    Classe de visualização para detalhar um aluno escolhido com métodos dependentes.
    """

    def get_object(self, id):
        # Tenta obter um aluno pelo ID e gera um erro Http404 se não for encontrado
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        # Obtém o objeto aluno com base no ID e serializa os dados para a resposta
        aluno = self.get_object(id)
        serializer = AlunoSerializer(aluno)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        # Obtém o objeto aluno com base no ID
        aluno = self.get_object(id)

        # Atualiza o objeto aluno com os dados da requisição
        serializer = AlunoSerializer(aluno, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        # Se os dados não forem válidos, retorna uma resposta de erro com os detalhes dos erros
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        # Obtém o objeto aluno com base no ID e o exclui
        aluno = self.get_object(id)
        aluno.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
