from rest_framework.views import APIView
from rest_framework.response import Response
from Controle.models.Tarefa import Tarefa
from Controle.serializers.TarefaSerializer import TarefaSerializer
from rest_framework import status
from django.http import Http404

class DetalhesTarefa(APIView):
   def get_object(self, id):
       try:
           return Tarefa.objects.get(id=id)
       except Tarefa.DoesNotExist:
           raise Http404

   def get(self, request, id, format=None):
       tarefa = self.get_object(id)
       serializer = TarefaSerializer(tarefa)
       return Response(serializer.data)

   def put(self, request, id, format=None):
       tarefa = self.get_object(id)
       serializer = TarefaSerializer(tarefa, data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

   def delete(self, request, id, format=None):
       tarefa = self.get_object(id)
       tarefa.delete()
       return Response(status=status.HTTP_204_NO_CONTENT)


  