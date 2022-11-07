# Modelo: [(id_aluno,nome,curso,tpc1,tpc2,tpc3,tpc4)]
import csv
import matplotlib.pyplot as plt


def lerAlunos():
    file1 = open("alunos.csv", encoding="UTF8")  
    file1.readline()    
    csv_file = csv.reader(file1,delimiter=",")
    lista11=[]
    for linha in csv_file:
        lista11.append(list(linha))
    return lista11

def distribCurso(alunos):
    dici = {}
    for _, _, curso, *_ in alunos:
        if curso in dici.keys():
            dici[curso] = dici[curso] + 1
        else:
            dici[curso] = 1
    return dici 

def medNotas(alunos):
    res1 = []
    for _, nome, _, tpc1, tpc2, tpc3, tpc4 in alunos:
        soma = (int(tpc1) + int(tpc2) + int(tpc3) + int(tpc4))
        media = soma/4
        res1.append((nome,media))
    return res1


def distrib1(alunos):
    plt.figure()
    plt.bar(alunos.keys(), alunos.values(), color="green")
    plt.xticks([x for x in range(0, len(alunos.keys()))], alunos.keys(), rotation = "vertical")
    plt.title(titulo)
    plt.show()


def distribEscalão(alunos):
    res3 = []
    for _, nome, _, _, _, _, _, media, *_ in alunos:
        media2 = float(media)
        if media2 < 5:
            res3.append((nome,"E"))
        elif media2 < 9:
            res3.append((nome,"D"))
        elif media2 < 13:
            res3.append((nome,"C"))
        elif media2 < 17:
            res3.append((nome,"B"))
        elif media2 < 21:
            res3.append((nome,"A"))     
    return res3

def datcomplt():
    data1 = lerAlunos()
    for i in range(len(lista11)):
        data1[i].append(lista11[1])
    return data1

def adcdat(data1):
    file2 = open("alunos.csv", encoding="UTF8", newline='') 
    writer = csv.writer(file2)
    writer.writerows(data1)

def distMedia(alunos):
    dc2 = {"[17,20] -> A":0, "[13,16.999] -> B":0, "[9,12.999] -> C":0, "[5,8.99] -> D":0, "[1,4.99] -> E":0}
    media1 = float(media)
    for _, _, _, _, _, _, _, media, *_ in alunos:
        if media < 5:
            dc2["[1,4.99] -> E"] = dc2["[1,4.99] -> E"] + 1
        elif media < 9:
            dc2["[5,8.99] -> D"] = dc2["[5,8.99] -> D"] + 1
        elif media < 13:
            dc2["[9,12.99] -> C"] = dc2["[9,12.99] -> C"] + 1
        elif media < 17:
            dc2["[13,16.999] -> B"] = dc2["[13,16.999] -> B"] + 1
        elif media < 21:
            dc2["[17,21] -> A"] = dc2["[17,21] -> A"] + 1
    return dc2

def CURSMED(alunos):
    res6 = []
    for _, _, curso, tpc1, tpc2, tpc3, tpc4, *_ in alunos:
        soma = (int(tpc1) + int(tpc2) + int(tpc3) + int(tpc4))
        media = soma/4
        res6.append((curso,media))
        c1 = [m for (cr,m) in res6 if cr == "LEI"]
        c2 = [m for (cr,m) in res6 if cr == "LCC"]
        c3 = [m for (cr,m) in res6 if cr == "ENGBIOM"]
        c4 = [m for (cr,m) in res6 if cr == "ENGFIS"]
        soma1 = sum(c1)/23
        soma2 = sum(c2)/20
        soma3 = sum(c3)/25
        soma4 = sum(c4)/32
    dic4 = dict([("LEI", round(soma1,1)),("LCC", round(soma2,1)),("ENGBIOM", round(soma3,1)),("ENGFIS", round(soma4,1))])
    return dic4

def distEscalao(alunos):
    res5 = []
    media2 = list(medNotas(alunos).items())
    for c in range (100):
        if media2 [c][1] < 5:
            res5.append((lerAlunos()[c][1], "E"))
        elif media2 [c][1] < 9:
            res5.append((lerAlunos()[c][1], "D"))
        elif media2 [c][1] < 13:
            res5.append((lerAlunos()[c][1], "C"))
        elif media2 [c][1] < 17:
            res5.append((lerAlunos()[c][1], "B"))
        elif media2 [c][1] < 21:
            res5.append((lerAlunos()[c][1], "A"))
    return res5
    dc3 = dict(res5)
    return dc3

#Definir agora uma função geral para criar os gráficos das respetivas distribuições
def Graf(distrib,titulo,abcissa,ordenada):
    y=list(distrib.values())
    x=list(distrib.keys()) 
    plt.ylabel(ordenada,rotation='vertical')
    plt.xlabel(abcissa)
    plt.title(titulo)
    plt.show()

#Tabelas
def tab1(): #média por curso
    print(f"{'':24} {':_^83'}")
    print(f"{'':21}|{'LEI':^21})|{'LCC':^21})|{'ENGBIOM':^21})|{'ENGFIS':^21}|")
    print(f"|{'Alunos:':^24}|{list(CURSMED(lerAlunos()).values())[0]:21}|{list(CURSMED(lerAlunos()).values())[1]:21}|{list(CURSMED(lerAlunos()).values())[2]:21}|{list(CURSMED(lerAlunos()).values())[3]:21}|")

def tab2(): #aluno por curso
    print(f"{'':24} {':_^83'}")
    print(f"{'':21}|{'ENGBIOM':^21})|{'ENGFIS':^21})|{'LEI':^21})|{'LCC':^21}|")
    print(f"|{'Alunos:':^24}|{list(distribCurso(lerAlunos()).values())[0]:21}|{list(distribCurso(lerAlunos()).values())[1]:21}|{list(distribCurso(lerAlunos()).values())[2]:21}|{list(distribCurso(lerAlunos()).values())[3]:21}|")

def tab3(): #aluno por escalão
    print(f"{'':24} {':_^83'}")
    print(f"{'':21}|{'ENGBIOM':^21})|{'ENGFIS':^21})|{'LEI':^21})|{'LCC':^21}|")
    print(f"|{'Alunos:':^24}|{list(distMedia(lerAlunos()).values())[0]:21}|{list(distMedia(lerAlunos()).values())[1]:21}|{list(distMedia(lerAlunos()).values())[2]:21}|{list(distMedia(lerAlunos()).values())[3]:21}|")



        


