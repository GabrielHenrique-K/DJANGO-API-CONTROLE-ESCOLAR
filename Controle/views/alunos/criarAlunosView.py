from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from Controle.models.Alunos import User
from Controle.serializers.AlunosSerializer import AlunoSerializer

class CriarAluno(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = AlunoSerializer




#utilizando APIVIEW SEM GENERICS como implementação. Acabei utilizando Gernerics pelo tempo, pois estava acontecendo um erro "Erro Circular".Acabei estudando Generics fazendo o metódo Put do Backend Samu, onde acabei aprendendo a usar Retrive

#from rest_framework import status
#from rest_framework.views import APIView
#from rest_framework.response import Response
#from Controle.models.Alunos import User
#from Controle.serializers.AlunosSerializer import AlunoSerializer
#
#class CriarAluno(APIView):
#    def post(self, request, *args, **kwargs):
#        serializer = AlunoSerializer(data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status=status.HTTP_201_CREATED)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    Cria uma "APIView" chamada "CriarAluno" que permite adicionar um novo aluno. Quando alguém faz uma solicitação de POST para esta API com os detalhes do aluno em formato JSON, o código verifica se os dados são válidos usando um "AlunoSerializer". 
    Se forem válidos, o aluno é adicionado e a resposta inclui os dados do aluno com um código de status.
