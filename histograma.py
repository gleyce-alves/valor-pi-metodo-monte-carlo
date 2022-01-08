"""
HISTOGRAMA - VALOR DE PI PELO MÉTODO DE MONTE CARLO
AUTORA: GLEYCE ALVES
"""
import re
import math
from collections import Counter
#Histograma

#Calculando a amplitude do histograma
numeros = [float(i) for i in re.findall(r"-?\d+\.?\d*", open("Valores de pi.txt").read())]

if numeros:
    print("Maior valor:", max(numeros))
    print("Menor valor:", min(numeros))
    print("Média:", sum(numeros)/len(numeros))

amplitude = (max(numeros) - min(numeros))
print ("A amplitude da amostra é:",amplitude)

#Definindo o número de classes:
n = sum(1 for line in open('Valores de pi.txt'))
classes = int(1 + 3.3*math.log10(n))
print(classes)
print(n)

#Cálculo de intervalos entre classes
ic = (amplitude/classes)
print("O intervalo de classes é:",ic)

#Calculando os extremos das classes:

limite_inferior = min(numeros)
limite_superior = limite_inferior + classes
print(limite_inferior, limite_superior)

# Contando as ocorrências de cada número:

n_pi = []

    #Carregar os valores de pi para listar:
    #fp é o próprio objeto de arquivo, você pode iterar sobre eles para obter as linhas no arquivo.
with open('Valores de pi.txt', 'r') as fp:
    for line in fp:
        if line != '\n':
            n_pi.append(line.lower().rstrip())

    #Criar um dicionário a partir da lista "n_pi":

cnt = Counter(n_pi)

    #Contando as ocorrências de Resultado_de_pi:
for k, v in cnt.items():
    print ('A ocorrência de ' + k + ' é: ' + str(v))

