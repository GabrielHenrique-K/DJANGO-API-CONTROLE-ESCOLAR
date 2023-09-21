from rest_framework import serializers
from Controle.models.Tarefa import Tarefa

class TarefaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarefa
        fields = ['titulo', 'descricao', 'data_entrega', 'concluida', 'aluno', 'disciplinas']
