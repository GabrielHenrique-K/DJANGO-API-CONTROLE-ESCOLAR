from rest_framework import generics
from Controle.models.Alunos import User
from Controle.serializers.AlunosSerializer import AlunoSerializer

class DetalhesAluno(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = AlunoSerializer
    lookup_field = 'id'