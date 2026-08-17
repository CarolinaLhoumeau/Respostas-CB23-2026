"""Atenção: código demora uns 1-3 minutos.
Para ir mais rápido, modifique a linha 32 em l_n
"""

#Iniciação e importações:
import time
import random as rd
from AP_03_ordenacao import selection_sort as sel_s
from AP_03_ordenacao import divide_and_conquer_sort as d_a_c_s
from AP_03_ordenacao import quick_sort as qui_s
import sys
sys.setrecursionlimit(max(10000, 6000))
rd.seed(1001)


#Fazer uma lista aleatória:
def make_lista_al(n):
    lista=[]
    for i in range(1,n+1):
        lista.append(i)
    rd.shuffle(lista)
    return lista

#Fazer lista "caso mais difícil":
def make_lista_inve(n):
    lista=[]
    for i in range(n+1,1,-1):
        lista.append(i)
    return lista

rep= 50 #=K
l_n=[100,500,1000,5000] #N
saida=[] #saida 1.0

for n in l_n:
    Al=make_lista_al(n)
    Hard=make_lista_inve(n)

    "Selection sort "
    "random"
    tempo=[]
    for i in range(1, rep+1):
        inicio=time.perf_counter()
        sel_s(Al)
        fim=time.perf_counter()
        tempo.append(fim - inicio)
    t_med_sort1_mod1=sum(tempo)/len(tempo)

    "hard"
    tempo=[]
    for i in range(1, rep+1):
        inicio=time.perf_counter()
        sel_s(Hard)
        fim=time.perf_counter()
        tempo.append(fim - inicio)
    t_med_sort1_mod2=sum(tempo)/len(tempo)


    "Divide & Conquer sort"
    "random"
    tempo=[]
    for i in range(1, rep+1):
        inicio=time.perf_counter()
        d_a_c_s(Al)
        fim=time.perf_counter()
        tempo.append(fim - inicio)
    t_med_sort2_mod1=sum(tempo)/len(tempo)

    "hard"
    tempo=[]
    for i in range(1, rep+1):
        inicio=time.perf_counter()
        d_a_c_s(Hard)
        fim=time.perf_counter()
        tempo.append(fim - inicio)
    t_med_sort2_mod2=sum(tempo)/len(tempo)

    "Quick sort"
    "random"
    tempo=[]
    for i in range(1, rep+1):
        inicio=time.perf_counter()
        qui_s(Al)
        fim=time.perf_counter()
        tempo.append(fim - inicio)
    t_med_sort3_mod1=sum(tempo)/len(tempo)

    "hard"
    tempo=[]
    for i in range(1, rep+1):
        inicio=time.perf_counter()
        qui_s(Hard)
        fim=time.perf_counter()
        tempo.append(fim - inicio)
    t_med_sort3_mod2=sum(tempo)/len(tempo)


    saida.append([n,t_med_sort1_mod1,t_med_sort1_mod2,t_med_sort2_mod1,t_med_sort2_mod2,t_med_sort3_mod1,t_med_sort3_mod2]) 
    "Saida (linhas): [n, t11, t12, t21, t22, t31, t32]"


saida2=[] #saida 2.0
for i in range(len(saida)):
    N,t11,t12,t21,t22,t31,t32=saida[i][0],saida[i][1],saida[i][2],saida[i][3],saida[i][4],saida[i][5],saida[i][6]
    saida2.append([f"Algoritmo               | Cenário   | N     | Tempo Médio"])
    saida2.append([f"Selection sort          | random    | {  N  :<6}| {t11:.6f}"])
    saida2.append([f"Selection sort          | hard      | {  N  :<6}| {t12:.6f}"])
    saida2.append([f"Divide and Conquer sort | random    | {  N  :<6}| {t21:.6f}"])
    saida2.append([f"Divide and Conquer sort | hard      | {  N  :<6}| {t22:.6f}"])
    saida2.append([f"Quick sort              | random    | {  N  :<6}| {t31:.6f}"])
    saida2.append([f"Quick sort              | hard      | {  N  :<6}| {t32:.6f}"])
    saida2.append(['--------------------------------------------------------'])

for line in saida2: #printar saída final
    print(line[0])