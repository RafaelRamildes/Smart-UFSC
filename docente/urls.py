from django.urls import path
from . import views

app_name='aluno'

urlpatterns=[
    path('/',           views.home,name='home'),
    path('/avaliações', views.avalia,name='avalia'),
    path('/turmas',     views.turmas,name='turmas'),
    ]
