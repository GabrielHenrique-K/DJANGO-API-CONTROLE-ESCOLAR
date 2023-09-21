from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from Controle.models.Alunos import User
from Controle.serializers.AlunosSerializer import AlunoSerializer

class CriarAluno(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = AlunoSerializer