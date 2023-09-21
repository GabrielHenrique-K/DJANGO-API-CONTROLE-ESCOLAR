from rest_framework import generics
from Controle.models.Disciplina import  Disciplina
from Controle.serializers.DisciplinaSerializer import DisciplinaSerializer



class DetalhesDisciplina(generics.RetrieveUpdateDestroyAPIView):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer
    lookup_field = 'id'