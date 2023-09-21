from rest_framework import generics
from Controle.models.Alunos import User
from Controle.serializers.AlunosSerializer import AlunoSerializer

class ListarAlunos(generics.ListAPIView):

    queryset = User.objects.all()
    serializer_class = AlunoSerializer