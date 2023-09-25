
from Controle.models.Alunos import User
from Controle.models.Tarefa import Tarefa
from Controle.serializers.TarefaSerializer import TarefaSerializer
from Controle.models.Disciplina import Disciplina
from rest_framework import serializers
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response



class CriarTarefa(APIView):
    def post(self, request):
       
        serializer = TarefaSerializer(data=request.data)
       
        if serializer.is_valid():
           
            serializer.save()         
            
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)