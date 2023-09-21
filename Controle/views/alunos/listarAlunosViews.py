from rest_framework import generics
from Controle.models.Alunos import User
from Controle.serializers.AlunosSerializer import AlunoSerializer

class ListarAlunos(generics.ListAPIView):

    queryset = User.objects.all()
    serializer_class = AlunoSerializer



#from rest_framework.views import APIView
#from rest_framework.response import Response
#from Controle.models.Alunos import User
#from Controle.serializers.AlunosSerializer import AlunoSerializer
#
#class ListarAlunos(APIView):
#    def get(self, request, format=None):
#        alunos = User.objects.all()
#        serializer = AlunoSerializer(alunos, many=True)
#        return Response(serializer.data)

    Get retorna todos os metodos criados para listagem.