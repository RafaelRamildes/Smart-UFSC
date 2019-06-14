from django.shortcuts import render
from math import ceil

class Professor:
    """Serve para definir as turmas, provas...
    """

Gat_Costa=Professor()
Gat_Costa.name="Gat Costa"
Gat_Costa.turmas=['1202','1220','1205','1003']
Gat_Costa.quant_turm=len(Gat_Costa.turmas)
Gat_Costa.provas_marcadas=3
Gat_Costa.provas_feitas=2
Gat_Costa.trab_marcados=None
Gat_Costa.ausencias_provas=['Aluno 09271500', 'Aluno 09271501', 'Aluno 09271502']
Gat_Costa.aulas_pra_turma=['Quarta-Feira','Sexta-Feira']

another_teacher=Professor()
another_teacher.name="Alguém"
another_teacher.turmas=[1202,1220,1205,1003]
another_teacher.quant_turm=len(Gat_Costa.turmas)
another_teacher.provas_marcadas=3
another_teacher.provas_feitas=2
another_teacher.trab_marcados={1220:'prisma',1202:'esfera',1003:'elipsoide'}
another_teacher.ausencias_provas=None
another_teacher.aulas_pra_turma=['Terça-Feira','Quinta-Feira']

def home(request):
    return render(
        request,
r"..\templates\layout-Geral2.html",
        {'top':-19,                                                 # Fator de correção da altura do navdiv     (OBRIGATÓRIO)
         'professor':Gat_Costa,                                     # Conta logada                              (OBRIGATÓRIO)
         }
        )

def avalia(request):
    try:
        w=1020/len(Gat_Costa.trab_marcados)-20   
    except:
        w=0
    t=ceil( Gat_Costa.quant_turm/2 ) 
    return render(
        request,
r"..\templates\layout-provasEtrabalhos2.html",    
        {'top':-19,                                                 # Fator de correção da altura do navdiv     (OBRIGATÓRIO)
         'professor':Gat_Costa,                                     # Conta logada                              (OBRIGATÓRIO)
         'width_prov':1020/Gat_Costa.quant_turm-20,                 # Correção do width de "Próximas    Provas"
         'width_trab':w,                                            # Correção do width de "Próximas Trabalhos"
         'before_lines':Gat_Costa.turmas[:t],                       # Primeira coluna da média de cada turma
         'after_lines':Gat_Costa.turmas[t:],                        # Segunda  coluna da média de cada turma
         'len_med_not':len(Gat_Costa.turmas[:t])*170,               # Correção da altura da  segunda  coluna
         }
        )

def turmas(request):
    return render (
        request,
r"..\templates\layout-PorTurmas.html",
        {'top':-19,                                                 # Fator de correção da altura do navdiv                  (OBRIGATÓRIO)
         'professor':Gat_Costa,                                     # Conta logada                                           (OBRIGATÓRIO)
         'range_prov':range(Gat_Costa.provas_marcadas),             # Diz quantas vezes se repete a div em "p1,p2,p3"
         'width_prov':1020/Gat_Costa.provas_marcadas-20,            # Dá o tamanho das div de "p1,p2,p3"
         'width_ausen':1020/len(Gat_Costa.ausencias_provas)-20,     # Dá o tamanho das div de "Ausencias em prova" se houver 
         'aulas':Gat_Costa.aulas_pra_turma,                         # Dá a data  das aulas de  determinada  turma
         'width_aulas':1020/len(Gat_Costa.aulas_pra_turma)-20,      # Determina  o tamanho das div de "aulas"
         }
        )
