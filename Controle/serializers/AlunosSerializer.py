from rest_framework import serializers
from Controle.models.Alunos import User

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


