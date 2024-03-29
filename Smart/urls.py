"""Smart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls.conf import include
from django.contrib import admin
from django.urls import path

urlpatterns = [

    path('',                        include('public.urls', namespace= 'public')),
    path('signup/',                 include('public.urls', namespace= 'public')),
    path('accounts/',               include('public.urls', namespace= 'public')),
    path('secret/',                 include('public.urls', namespace= 'public')),
    
    path('/Aluno',                  include( 'aluno.urls', namespace = 'aluno')),
    path('/Matérias',               include( 'aluno.urls', namespace = 'aluno')),
    path('/disciplina',             include( 'aluno.urls', namespace = 'aluno')),
    path('/ProvasETrabalhos',       include( 'aluno.urls', namespace = 'aluno')),

    path('/Docente',                include('docente.urls',namespace='docente')),
    path('/avaliação',              include('docente.urls',namespace='docente')),
    path('/turmas',                 include('docente.urls',namespace='docente')),
    
    path('admin/', admin.site.urls),
]
