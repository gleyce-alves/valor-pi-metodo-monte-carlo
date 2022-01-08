"""ESTIMANDO O VALOR DE PI PELO MÉTODO DE MONTE CARLO
AUTORA: GLEYCE ALVES
"""
import math
import random

#PARÂMETROS

Nquadrado = 50000 #quanto maior o número de pontos, melhor a precisão do valor de pi

for i in range(50000):

    Ncirculo = 0

    acumulador = 1
    while acumulador <= Nquadrado:
        Px = random.random() #coordenada x do ponto P
        Py = random.random() #coordenada y do ponto P
        deltaX = math.pow((Px - 0.5),2) #variação de X
        deltaY = math.pow((Py-0.5),2) #variação de Y
        DistE = math.sqrt(deltaX+deltaY) #cálculo da distância entre a origem e o ponto selecionado
        if DistE < 0.5:
            Ncirculo = Ncirculo + 1
        acumulador = acumulador + 1

    Resultado_de_pi = 4*(float(Ncirculo))/(float(Nquadrado))

    print ("Pi tem o valor aproximado de %.2f" %Resultado_de_pi)
    arquivo = open('Valores de pi.txt','a')  
    arquivo.write("{:.2f}".format(Resultado_de_pi) + "\n")  
    arquivo.close()

