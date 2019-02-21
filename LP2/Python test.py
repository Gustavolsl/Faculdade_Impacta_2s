
'''def merge(L1,L2):
    L3=[]
    i1=i2=0
    while i1<len(L1) and i2<len(L2): #L1 = Lista1, L2 = Lista2
        if L1[i1]<L2[i2]:
            L3.append(lista2[i2])
            i1=i1+1
        else:
            L3.append(L2[i2])
            i2=i2+1
    #Lista3 = lista3 + lista{i1:]+lista2[i2:]'''

#Fazendo de outro modo (Melhor):
            
while i1<len(L1):
    L3.append(L1[i1])
    i1=i1+1
while i2<len(L2):
    L3.append(L2[i2])
    i2=i2+1
return L3



'''from math import sqrt

def primoRapido(n):
    if n == 1:
        return False
    for i in range(2,int(sqrt(n))+1):  #De 2 até raiz de n
        if n % i == 0:
            return False
        return True:

def teste_primoRapido():
    if primeRapido(1) !=False:
        return False
    elif primoRapido(2) !=True:
        return False
    elif primoRapido(7) !=True:
        return False
    elif primoRapido(11) !=True:
        return False
    elif primoRapido(15) !=False:
        return False
    elif primoRapido(123) !=False:
        return False
    else:
        return 
    















































































































