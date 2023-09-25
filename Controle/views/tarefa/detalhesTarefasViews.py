from rest_framework.views import APIView
from rest_framework.response import Response
from Controle.models.Tarefa import Tarefa
from Controle.serializers.TarefaSerializer import TarefaSerializer
from rest_framework import status
from django.http import Http404

class DetalhesTarefa(APIView):
    """
    Classe de visualização para detalhar uma tarefa com métodos dependentes.
    """

    def get_object(self, id):
        # Tenta obter uma tarefa pelo ID e gera um erro Http404 se não for encontrada
        try:
            return Tarefa.objects.get(id=id)
        except Tarefa.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        # Obtém o objeto tarefa com base no ID e serializa os dados para a resposta
        tarefa = self.get_object(id)
        serializer = TarefaSerializer(tarefa)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        # Obtém o objeto tarefa com base no ID
        tarefa = self.get_object(id)

        # Atualiza o objeto tarefa com os dados da requisição
        serializer = TarefaSerializer(tarefa, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        # Se os dados não forem válidos, retorna uma resposta de erro com os detalhes dos erros
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        # Obtém o objeto tarefa com base no ID e o exclui
        tarefa = self.get_object(id)
        tarefa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
