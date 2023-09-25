from rest_framework import serializers
from Controle.models.Alunos import User

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        # Define o modelo associado ao serializador
        model = User
        
        # Define quais campos do modelo serão serializados
        fields = '__all__'
