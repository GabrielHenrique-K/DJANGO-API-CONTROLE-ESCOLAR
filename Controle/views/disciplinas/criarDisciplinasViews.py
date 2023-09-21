from rest_framework import generics
from Controle.models.Disciplina import Disciplina
from Controle.serializers.DisciplinaSerializer import DisciplinaSerializer



class CriarDisciplina(generics.CreateAPIView):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer




#from rest_framework.views import APIView
#from rest_framework.response import Response
#from Controle.models.Disciplina import Disciplina
#from Controle.serializers.DisciplinaSerializer import DisciplinaSerializer
#from rest_framework import status
#
#class CriarDisciplina(APIView):
#    def post(self, request, format=None):
#        serializer = DisciplinaSerializer(data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status=status.HTTP_201_CREATED)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #Uma "APIView" chamada "CriarDisciplina" que é responsável por criar uma nova disciplina. Quando um pedido HTTP POST é feito para esta API com os detalhes da disciplina em formato JSON.