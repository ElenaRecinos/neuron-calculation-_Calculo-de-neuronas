"""Ejercicio #1:

Calcular la salida de una neurona mediante la funcion sigmoide para estimar la probabilidad de que un estudiante apruebe una evaluacion.

Un sistema inteligente analiza dos entradas: horas de estudio y porcentaje de tareas completadas.

Horas de estudio (X1): 6
Tareas completadas (X2): 0.8
W1: 0.7
W2: 0.5
Sesgo (b): -3 """

import math


#variables
x1 = 6
x2 = 0.8
w1 = 0.7
w2 = 0.5
b = 3

# calculo de la funcion z
# z = (x1*w1) + (x2*w2) -b

x1w1 = x1*w1
x2w2 = x2*w2

z = x1w1 + x2w2 -b
print(round(z, 2)) # usamos round para redondear el resultado a 2 decimales


# calculo de la funcion sigmoide
# sigmoide = 1/(1+e^-z)

def sigmoide(z):
    return 1/(1+math.exp(-z))

print(round(sigmoide(z), 4)) 













