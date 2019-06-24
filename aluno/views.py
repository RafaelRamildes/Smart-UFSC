from django.shortcuts import render
from django.contrib.auth.decorators import login_required


'==============================================================================================================='
#Criação de Classes

class Aluno:
    """define atributos do aluno"""

class Materia:
    """define atributos de materias"""

EGR5606=Materia()
EGR5606.name="Desenho Técnico"
EGR5606.codigo="EGR5606"

EGR5606.prox_tarefas=['Tarefa: SolidWorks 09','Tarefa: SolidWorks 10']
EGR5606.prox_prov=[]#'Prova: 23/34','Prova: 45/90'] #Definido para texte
EGR5606.aulas=['Aula: Sexta-Feira','Aula: Quarta-Feira']
EGR5606.tarefas=[
    "Vistas Ortográficas - Parte 1",
    "Vistas Ortográficas - Parte 2",
    "Vistas Ortográficas - Parte 3",
    "SolidWorks - Exercícios 1",
    "SolidWorks - Exercícios 2",
    "SolidWorks - Exercícios 3",
    "SolidWorks - Exercícios 4",
    "SolidWorks - Exercícios 5",
    "SolidWorks - Exercícios 6",
    "SolidWorks - Exercícios 7",
    "SolidWorks - Exercícios 8",
    "SolidWorks - Exercícios 9",
                 ]

Subway=Aluno()
Subway.name="Subway"

Subway.materias={
    'Desenho Técnico': 'EGR5806',
    'Cálculo I': 'MTM3101',
    'Geometria Analítica': 'MTM5512',
    'Física I': 'FSC5101',
    'Introdução À Engenharia de Controle E Automação':'DAS5411',
    'Introdução À Informática Para Automação': 'DAS5334'
    }

Subway.professores=[
    'Felipe Gomes de Oliveira Cabral',
    'Fábio Luís Baldissera',
    'Hector Bessa Silveira',
    'Romulo Adolfo Heringer Ferreira',
    'Cristiani Campos Pia Cid',
    'Camila Aparecida Banedito Rodrigues de Lima',
    'Gustavo Adolfo Torres Fernandes da Costa',
    ]

Subway.proximos_trab=[
    'Simulador de trafego',
    'Protótipo 3',
    'Simulador de vírus',
    'Expolouro',
    ]

Subway.trab_feitos=[
    'Protótipo 1',
    'Protótipo 2',
    ]

'==============================================================================================================='
#Definições das views

@login_required
def index(request):
    l=len(Subway.materias)
    div=l//3
    return render(
        request,
        r"..\templates\layout-Geral.html",
        {'materias':Subway.materias.keys(),                 # Serve para a dropdown " mate´rias "                                   (OBRIGATÓRIO)
         'professores':Subway.professores,                  # Serve para a dropdown "professores"                                   (OBRIGATÓRIO)
         'coluna1':list(Subway.materias.keys())[:div],      # Faz das chaves do dicionário uma lista e extrai só os primeiros itens
         'coluna2':list(Subway.materias.keys())[div:2*div], # Faz das chaves do dicionário uma lista e extrai só os itens do meio
         'coluna3':list(Subway.materias.keys())[2*div:],    # Faz das chaves do dicionário uma lista e extrai só os útimos itens
         'correcao':300*div+30*div,                         # Corrigir a posiçãoY das colunas *
         }
        )

@login_required
def materias(request):
    return render(
        request,
        r"..\templates\layout-Materias.html",
        {'materias':Subway.materias.keys(),                 # Serve para a cropdown " mate´rias "   (OBRIGATÓRIO)
         'professores':Subway.professores,                  # Serve para a dropdown "professores"   (OBRIGATÓRIO)
         }
        )

@login_required
def cadeira(request):
    #v=request.GET["disciplina"]
    s1=None
    s2=None
    
    #<----Define o que estará nos slots, dando prioridade para "prova"-"trabalho"
    if EGR5606.prox_prov:                                   
        s1=EGR5606.prox_prov[0]                             
        if EGR5606.prox_tarefas:                        
            s2=EGR5606.prox_tarefas[0]
        elif len(EGR5606.prox_prov)>=2:
            s2=EGR5606.prox_prov[1]
            
    elif EGR5606.prox_tarefas:                              
        s1=EGR5606.prox_tarefas[0]                        
        if len(EGR5606.prox_tarefas)>=2:                  
            s2=EGR5606.prox_tarefas[1]
        
            
    return render(
        request,
        r"..\templates\layout-porMateria.html",
        {'materias':Subway.materias.keys(),                 # Serve para a cropdown " mate´rias "                                                       (OBRIGATÓRIO)
         #'título':v,                                       # Possuia serventia para um sistema que ainda não foi feito (ainda que isso seja paradoxal)
         'professores':Subway.professores,                  # Serve para a dropdown "professores"                                                       (OBRIGATÓRIO)
         'prox_aula':EGR5606.aulas[0],                      # Anuncia a próxima aula (Há de ser feito um sistema para descobrir qual a próxima aula)
         'slot1':s1,                                        # Um slot para prova ou trabalho
         'slot2':s2,                                        # Um slot para prova ou trabalho
         'tarefas':EGR5606.tarefas,                         # Passa uma lista com todas as tarefas
         }
        )

@login_required
def Notas(request):
    
    l=len(Subway.materias)
    div=l//3                                                # Ex.:[iten1,iten2<div>iten3,iten4<2*div>iten5]

    overflow="none"
    if len(Subway.proximos_trab) > 3:                       # Para averiguar a necessidade de um scroll
        overflow="auto"
        
    return render(
        request,
        r"..\templates\layout-provasEtrabalhos.html",
        {'materias':Subway.materias.keys(),                 # Serve para a cropdown " mate´rias "                                   (OBRIGATÓRIO)
         'professores':Subway.professores,                  # Serve para a dropdown "professores"                                   (OBRIGATÓRIO)
         'coluna1':list(Subway.materias.keys())[:div],      # Faz das chaves do dicionário uma lista e extrai só os primeiros itens
         'coluna2':list(Subway.materias.keys())[div:2*div], # Faz das chaves do dicionário uma lista e extrai só os itens do meio
         'coluna3':list(Subway.materias.keys())[2*div:],    # Faz das chaves do dicionário uma lista e extrai só os útimos itens
         'correcao':200*div + 20*div,                       # Corrigir a posiçãoY das colunas *
         'proximos':Subway.proximos_trab,                   # Passa os trabalhos que virão
         'scroll':overflow,                                 # Adiciona um scroll no overflowX em "próximos trabalhos" se houver necessidade
         'feitos':Subway.trab_feitos                        # Passodo com a única função de camuflar divs caso não haja 
         }
        )



"""
NOTA:  *Mulptiplica a altura dos blocos de matérias pela quantidade de matérias em cada coluna mais a
        distância entre os blocos e quantas vezes há essa distância, isso para
"""
