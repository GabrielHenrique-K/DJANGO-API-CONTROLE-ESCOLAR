from rest_framework.views import APIView
from rest_framework.response import Response
from Controle.models.Disciplina import Disciplina
from Controle.serializers.DisciplinaSerializer import DisciplinaSerializer

class ListarDisciplinas(APIView):
    """
    Classe de visualização para listar todas as disciplinas com seus IDs, nomes e descrições.
    """

    def get(self, request, format=None):
        # Obtém todas as disciplinas do banco de dados
        disciplinas = Disciplina.objects.all()

        # Serializa a lista de disciplinas para a resposta
        serializer = DisciplinaSerializer(disciplinas, many=True)

        # Retorna a lista de disciplinas serializadas
        return Response(serializer.data)
