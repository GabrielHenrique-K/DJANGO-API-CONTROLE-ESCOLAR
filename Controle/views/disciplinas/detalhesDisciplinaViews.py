from rest_framework.views import APIView
from rest_framework.response import Response
from Controle.models.Disciplina import Disciplina
from Controle.serializers.DisciplinaSerializer import DisciplinaSerializer
from rest_framework import status
from django.http import Http404

class DetalhesDisciplina(APIView):
    """
    Classe de visualização para detalhar uma disciplina com métodos dependentes.
    """
    
    def get_object(self, id):
        # Tenta obter uma disciplina pelo ID e gera um erro Http404 se não for encontrada
        try:
            return Disciplina.objects.get(id=id)
        except Disciplina.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        # Obtém o objeto disciplina com base no ID e serializa os dados para a resposta
        disciplina = self.get_object(id)
        serializer = DisciplinaSerializer(disciplina)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        # Obtém o objeto disciplina com base no ID
        disciplina = self.get_object(id)

        # Atualiza o objeto disciplina com os dados da requisição
        serializer = DisciplinaSerializer(disciplina, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        # Se os dados não forem válidos, retorna uma resposta de erro com os detalhes dos erros
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        # Obtém o objeto disciplina com base no ID e o exclui
        disciplina = self.get_object(id)
        disciplina.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
