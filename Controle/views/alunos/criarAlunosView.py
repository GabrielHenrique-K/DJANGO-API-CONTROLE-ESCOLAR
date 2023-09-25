

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from Controle.models.Alunos import User
from Controle.serializers.AlunosSerializer import AlunoSerializer

class CriarAluno(APIView):
   def post(self, request, *args, **kwargs):
       serializer = AlunoSerializer(data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

