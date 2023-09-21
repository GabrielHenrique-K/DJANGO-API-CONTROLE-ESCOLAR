from rest_framework import generics
from Controle.models.Disciplina import  Disciplina
from Controle.serializers.DisciplinaSerializer import DisciplinaSerializer



class DetalhesDisciplina(generics.RetrieveUpdateDestroyAPIView):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer
    lookup_field = 'id'


#from rest_framework.views import APIView
#from rest_framework.response import Response
#from Controle.models.Disciplina import Disciplina
#from Controle.serializers.DisciplinaSerializer import DisciplinaSerializer
#from rest_framework import status
#from django.http import Http404

#class DetalhesDisciplina(APIView):
#    def get_object(self, id):
#        try:
#            return Disciplina.objects.get(id=id)
#        except Disciplina.DoesNotExist:
 #           raise Http404
#
 #   def get(self, request, id, format=None):
 #       disciplina = self.get_object(id)
 #       serializer = DisciplinaSerializer(disciplina)
 #       return Response(serializer.data)
#
#    def put(self, request, id, format=None):
 #       disciplina = self.get_object(id)
  #      serializer = DisciplinaSerializer(disciplina, data=request.data)
  #      if serializer.is_valid():
  #          serializer.save()
   #         return Response(serializer.data)
   #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
   # def delete(self, request, id, format=None):
   #     disciplina = self.get_object(id)
   #     disciplina.delete()
   #     return Response(status=status.HTTP_204_NO_CONTENT)

    #"DetalhesDisciplina" que lida com operações de busca, atualização e exclusão de informações de uma disciplina específica. A função get_object verifica se uma disciplina com o ID especificado existe no banco de dados e lança um erro 404 caso contrário.