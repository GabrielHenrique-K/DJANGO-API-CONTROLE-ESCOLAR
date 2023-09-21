from rest_framework import generics
from Controle.models.Alunos import User
from Controle.serializers.AlunosSerializer import AlunoSerializer

class DetalhesAluno(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = AlunoSerializer
    lookup_field = 'id'



#from rest_framework import status
#from rest_framework.views import APIView
#from rest_framework.response import Response
#from Controle.models.Alunos import User
#from Controle.serializers.AlunosSerializer import AlunoSerializer
#from django.http import Http404
#
#class DetalhesAluno(APIView):
#    def get_object(self, id):
#        try:
#            return User.objects.get(id=id)
#        except User.DoesNotExist:
#            raise Http404
#
#    def get(self, request, id, format=None):
#        aluno = self.get_object(id)
#        serializer = AlunoSerializer(aluno)
#        return Response(serializer.data)
#
#    def put(self, request, id, format=None):
#        aluno = self.get_object(id)
#        serializer = AlunoSerializer(aluno, data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#    def delete(self, request, id, format=None):
#        aluno = self.get_object(id)
#        aluno.delete()
#        return Response(status=status.HTTP_204_NO_CONTENT)

    Implementa uma "APIView" chamada "DetalhesAluno" que lida com as operações de busca, atualização e exclusão de informações de um aluno específico. A função get_object verifica se um aluno com o ID especificado existe no banco de dados e lança um erro 404 caso contrário. 
