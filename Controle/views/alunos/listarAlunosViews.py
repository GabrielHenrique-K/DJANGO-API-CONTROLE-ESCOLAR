from rest_framework.views import APIView
from rest_framework.response import Response
from Controle.models.Alunos import User
from Controle.serializers.AlunosSerializer import AlunoSerializer

class ListarAlunos(APIView):
    """
    Detalha todos os alunos criado no Criar Alunos View. Junto a seu ID, nome, email.
    """
    def get(self, request, format=None):
       alunos = User.objects.all()
       serializer = AlunoSerializer(alunos, many=True)
       return Response(serializer.data)
