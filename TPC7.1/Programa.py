import Aulan7

Menu = str("""Escolha uma das seguintes opções:
0 - Sair
1 - Carregar os dados para uma lista
2 - Distribuição dos alunos por curso
3 - Dataset atualizado com a média das notas de cada aluno 
4 - Coluna com os escalões
5 - Dataset atualizado com as duas novas colunas
6 - Gráficos com as distribuições
7 - Tabelas com as distribuições
""")

print(Menu)

n = 11

while n!=0:
    alunos = Aulan7.lerAlunos()
    n = int(input("Introduza a opção escolhida:"))
    if n == 1:
        print(f"{'Lista de alunos':=^106}")
        print(Aulan7.lerAlunos())
    elif n == 2:
        print(f"{'Distribuição dos alunos por cursos:':=^20}")
        print(Aulan7.distribCurso(alunos))
    elif n == 3:
        print(f"{'Médias dos trabalhos':=^106}")
        print(Aulan7.medNotas(alunos))
        print(f"{'Dataset atualizado com as médias':=^106}")
        print(Aulan7.adcdat(Aulan7.medNotas(alunos)))
    elif n == 4:
        print(f"{'Escalões':=^106}")
        print(Aulan7.distribEscalão(alunos))
        print(f"{'Dataset com os escalões':=^106}")
        pritn(Aulan7.adcdat(Aulan7.distribEscalão(alunos)))
    elif n == 5:
        print(f"{'Dataset atualizado':=^106}")
        print(f"{'id':^10}|{'nome':^10}|{'curso':^10}|{'tpc1':^6}|{'tpc2':^6}|{'tpc3':^6}|{'tpc4':^6}|{'média':^6}|{'grau':^6}")
        for c in range(100):
            print(f"{Aulan7.lerAlunos()[c][0]:^10}|{Aulan7.lerAlunos()[c][1]:^10}|{Aulan7.lerAlunos()[c][2]:^10}|{Aulan7.lerAlunos()[c][3]:^10}|{Aulan7.lerAlunos()[c][4]:^10}|{Aulan7.lerAlunos()[c][5]:^10}|{Aulan7.lerAlunos()[c][6]:^10}")
    elif n == 6:
        n1 = 5 
        while n1 != 0:
            menu1 = (str("""Distribuições:
            1 - Alunos por curso
            2 - Alunos por escalão
            3 - Médias por curso """))
            n1 = int(input("Introduza a opção do menu1"))
            if n == 1:
                print("Gráfico de Linha")
                print(Aulan7.Graf(Aulan7.distribCurso(Aulan7.lerAlunos())),"Distribuição dos alunos por curso","Curso","Número de alunos")
            if n == 2:
                print("Gráfico de Linha")
                print(Aulan7.Graf(Aulan7.distMedia(Aulan7.lerAlunos())),"Distribuição dos alunos por curso","Curso","Número de alunos")
            if n == 3:
                print("Gráfico de Linha")
                print(Aulan7.Graf(Aulan7.CURSMED(Aulan7.lerAlunos())),"Distribuição dos alunos por curso","Curso","Número de alunos")

    elif n == 7:
        n2 = 6
        while n2 != 0:
            menu1 = (str("""Distribuições:
            1 - Alunos por curso
            2 - Alunos por escalão
            3 - Médias por curso """))
            if n == 1:
                print("Tabela com os alunos por curso")
                print(Aulan7.tab2())
            if n == 2:
                print("Tabela com os alunos por escalão")
                print(Aulan7.tab3())
            if n == 3:
                print("Tabela com as médias por curso")
                print(Aulan7.tab1())
if n == 0:
    print("Acabou de sair da aplicação")