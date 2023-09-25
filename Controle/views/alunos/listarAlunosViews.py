from rest_framework.views import APIView
from rest_framework.response import Response
from Controle.models.Alunos import User
from Controle.serializers.AlunosSerializer import AlunoSerializer

class ListarAlunos(APIView):
    """
    Classe de visualização para listar todos os alunos com seus IDs, nomes e emails.
    """

    def get(self, request, format=None):
        # Obtém todos os alunos do banco de dados
        alunos = User.objects.all()

        # Serializa a lista de alunos para a resposta
        serializer = AlunoSerializer(alunos, many=True)

        # Retorna a lista de alunos serializados
        return Response(serializer.data)
