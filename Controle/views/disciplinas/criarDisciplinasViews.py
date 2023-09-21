from rest_framework import generics
from Controle.models.Disciplina import Disciplina
from Controle.serializers.DisciplinaSerializer import DisciplinaSerializer



class CriarDisciplina(generics.CreateAPIView):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer
