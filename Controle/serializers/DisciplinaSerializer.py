from rest_framework import serializers
from Controle.models.Disciplina import Disciplina

class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        # Define o modelo associado ao serializador
        model = Disciplina
        
        # Define quais campos do modelo serão serializados
        fields = '__all__'
