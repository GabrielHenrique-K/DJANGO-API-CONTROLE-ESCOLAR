from rest_framework import serializers
from Controle.models.Tarefa import Tarefa
from Controle.models.Alunos import User
from Controle.models.Disciplina import Disciplina

class TarefaSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = Tarefa
        fields = '__all__'
