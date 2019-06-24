from django.urls import path
from . import views

app_name='aluno'

urlpatterns=[
    path('',                    views.index,    name = 'index'),
    path('Matérias/',           views.materias, name='materia'),
    path('disciplina/',         views.cadeira,  name='cadeira'),
    path('ProvasETrabalhos/',   views.Notas,    name = 'notas'),
    ]
