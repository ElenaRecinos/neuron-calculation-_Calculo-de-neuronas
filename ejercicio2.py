""" Ejercicio  #2:

Comparar las salidas de una misma neurona utilizando dos funciones de activación diferentes.

Una empresa analiza el crecimiento de las ventas según la inversión publicitaria y la satisfacción del cliente.

Calcular la suma ponderada, la función Sigmoide y Tanh. Además demostrar el rango de salida.

Inversión publicitaria normalizada (X1): 0.7
Satisfacción del cliente normalizada (X2): 0.9
W1: 0.8
W2: 0.6
B: -0.4  """

import math

 # Variables
x1 = 0.7
x2 = 0.9
w1 = 0.8
w2 = 0.6
b = 0.4

# calculo de la funcion z
# z = (x1*w1) + (x2*w2) -b

x1w1 = x1*w1
x2w2 = x2*w2

z = x1w1 + x2w2 -b
print("Suma ponderada:", round(z, 2)) # suma ponderada

#Sigmoide
def sigmoide(z):
    return 1/(1+math.exp(-z))

print("sigmoide = ", round(sigmoide(z), 4)) # sigmoide 0.6682

#Tanh
def tanh(z):
    return math.tanh(z)

print("tanh = ", round(tanh(z), 4)) # tanh 0.5778












