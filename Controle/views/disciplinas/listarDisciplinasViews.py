from rest_framework import generics
from Controle.models.Disciplina import  Disciplina
from Controle.serializers.DisciplinaSerializer import  DisciplinaSerializer






class ListarDisciplinas(generics.ListAPIView):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer




#from rest_framework.views import APIView
#from rest_framework.response import Response
#from Controle.models.Disciplina import Disciplina
#from Controle.serializers.DisciplinaSerializer import DisciplinaSerializer

#class ListarDisciplinas(APIView):
#    def get(self, request, format=None):
#        disciplinas = Disciplina.objects.all()
#        serializer = DisciplinaSerializer(disciplinas, many=True)
#        return Response(serializer.data)
