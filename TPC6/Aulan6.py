# Modelo: [(nome,descrição,ano de Criação,período,compositor,duração,_id)]

import csv
from turtle import color
import matplotlib.pyplot as plt

def lerObras():
    file = open("obras.csv", encoding="UTF8")  #Colocamos assim porque o ficheiro está na pasta onde o ficheiro principl se encontra
    file.readline()    #permite passar uma linha à frente 
    csv_file = csv.reader(file,delimiter=";")
    lista=[]
    for linha in csv_file:
        lista.append(tuple(linha))
    return lista

def contarObras(obras):
    file = open("obras.csv", encoding="UTF8")  #Colocamos assim porque o ficheiro está na pasta onde o ficheiro principl se encontra
    file.readline()    #permite passar uma linha à frente 
    csv_file = csv.reader(file,delimiter=";")
    lista1=[]
    for linha in csv_file:
        lista1.append(tuple(linha))
    return len(lista1)

def imprimeObras(obras):
    print(f"| {'Nome':20} | {'Descrição':25} | {'Ano':8} | {'Compositor':15} |")
    for nome, desc, ano, _, comp, *_ in obras:
        print(f"| {nome[:20]:20} | {desc[:25]:25} | {ano:8} | {comp[:15]:15} |")

def ordem(tuplo):
    return tuplo[0]
def ordenar(obras):
    lista = []
    for nome, _, ano, *_ in obras:
        lista.append((nome,ano))
    lista.sort(key=ordem)
    return lista

def ordem1(tuplo):
    return tuplo[1]
def ordenar1(obras):
    lista1 = []
    for nome,_,ano,*_ in obras:
        lista1.append((nome,ano))
    lista1.sort(key=ordem1)
    return lista1

def ordem2(obras):
    lista2 = []
    for _, _, _, _, comp, *_ in obras:
        lista2.append(comp)
    return sorted(lista2)

def distPeriodo(obras):
    dici = {}
    for _, _, _, periodo, *_ in obras:
        if periodo in dici.keys():
            dici[periodo] = dici[periodo] + 1
        else:
            dici[periodo] = 1
    return dici  

def distNP(obras):
    d0= {}
    for nome, _, _, periodo, *_ in obras:
        if periodo in d0.keys():
            d0[periodo].append(nome)
        else:
            d0[periodo] = [nome]
    return d0

def distbAno(obras):
    d = {}
    for _, _, ano, *_ in obras:
        if ano in d.keys():
            d[ano] = d[ano] + 1
        else:
            d[ano] = 1
    return d 

def distNT(obras):
    d1 = {}
    for nome, _, ano, *_ in obras:
        if ano in d1.keys():
            d1[ano].append(nome)   
        else:
            d1[ano] = [nome]
    return d1

def dCPTOR(obras):
    d2 = {}
    for _, _, _, _, comp, *_ in obras:
        if comp in d2.keys():
            d2[comp] = d2[comp] + 1
        else:
            d2[comp] = 1
    return d2

def distNC(obras):
    d3 = {}
    for nome, _, _, _, comp, *_ in obras:
        if comp in d3.keys():
            d3[comp].append(nome)
        else:
            d3[comp] = [nome]
    return d3

def distribuico(ob1):
    plt.figure(fsize=(30,15))
    plt.bar(obras.keys(), obras.values(), color="green")
    plt.xticks([x for x in range(0, len(obras.keys()))], obras.keys(), rotation = "vertical")
    plt.show()

def distribuico1(ob2):
    plt.figure(fsize=(30,15))
    plt.bar(obras.keys(), obras.values(), color="green")
    plt.xticks([x for x in range(0, len(obras.keys()))], obras.keys(), rotation = "vertical")
    plt.show()

def distribuico2(ob3):
    plt.figure(fsize=(30,15))
    plt.bar(obras.keys(), obras.values(), color="green")
    plt.xticks([x for x in range(0, len(obras.keys()))], obras.keys(), rotation = "vertical")
    plt.show()

def COMPOBRAS(obras):
    d4 = zip(obras.keys(), obras.values())
    lista3 = list(d4)
    return lista3 