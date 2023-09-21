"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from Controle.views.alunos.criarAlunosView import CriarAluno
from Controle.views.alunos.detalhesAlunosViews import DetalhesAluno
from Controle.views.alunos.listarAlunosViews import ListarAlunos

from Controle.views.tarefa.criarTarefasViews import CriarTarefa
from Controle.views.tarefa.detalhesTarefasViews import DetalhesTarefa
from Controle.views.tarefa.listarTarefasAlunoViews import ListarTarefasAluno
from Controle.views.tarefa.listarTarefasViews import ListarTarefas

from Controle.views.disciplinas.criarDisciplinasViews import CriarDisciplina
from Controle.views.disciplinas.detalhesDisciplinaViews import DetalhesDisciplina
from Controle.views.disciplinas.listarDisciplinasViews import ListarDisciplinas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('controle/alunos/', ListarAlunos.as_view()),
    path('controle/alunos/<int:id>/', DetalhesAluno.as_view()),
    path('controle/alunos/<int:aluno_id>/tarefas/', ListarTarefasAluno.as_view()),
    path('controle/disciplinas/', ListarDisciplinas.as_view()),
    path('controle/disciplinas/<int:id>/', DetalhesDisciplina.as_view()),
    path('controle/tarefas/', ListarTarefas.as_view()),
    path('controle/tarefas/<int:id>/', DetalhesTarefa.as_view()),
]

