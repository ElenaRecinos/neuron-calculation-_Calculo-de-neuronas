""" Ejercicio #3:

Un banco desea desarrollar una red neuronal artificial que ayude a identificar transacciones bancarias sospechosas. El sistema analiza tres variables normalizadas para determinar si una transacción presenta indicios de fraude.

Capa 1:

Monto de la transacción normalizado X1: 0.8
Frecuencia de transacciones sospechosas X2: 0.6
Indicador de ubicación inusual X3: 0.9
Sesgo b1: -0.2
Capa 2:

Peso de x1: w4 = -0.5

Peso de x2: w5 = 0.9

Peso de x3: w6 = 0.6

Sesgo: b2 = 0.1

La función de activación utilizada en ambas neuronas ocultas es la tangente hiperbólica (tanh).

Pesos y sesgo de la capa de salida:
Peso de h1: w7 = 1.2

Peso de h2: w8 = -0.8

Sesgo de salida: Y = 0.15

La función de activación de la neurona de salida es la sigmoide.

 """


#CAPA 1
import math 

# Variables de la capa 1
x1 = 0.8
x2 = 0.6
x3 = 0.9
w1 = 1
w2 = 1 # se asumen todos los pesos de la capa 1 como 1 para simplificar el cálculo
w3 = 1
b1 = 0.2

x1w1 = x1*w1
x2w2 = x2*w2
x3w3 = x3*w3

#Calculo de z1
z1 = x1w1 + x2w2 + x3w3 - b1
print("Suma ponderada de la capa 1 (z1):", round(z1, 4)) #2.1


#CAPA 2

#Variables de la capa 2
w4 = -0.5
w5 = 0.9
w6 = 0.6
b2 = 0.1

#Calculo de z2
x1x4 = x1*w4
x2w5 = x2*w5
x3w6 = x3*w6

z2 = x1x4 + x2w5 + x3w6 + b2
print("Suma ponderada de la capa 2 (z2):", round(z2, 4)) #0.78

# Definimos el tanh
def tanh(z):
    return math.tanh(z)

# llamamos la funcion usando como parametro cada funcion para tener las salidas de cada neurona oculta h1 y h2
h1 = tanh(z1)
h2 = tanh(z2)

print("Salida de h1:", round(h1, 4)) # 0.9705
print("Salida de h2:", round(h2, 4)) # 0.6527

#CAPA DE SALIDA
w7 = 1.2
w8 = -0.8
Y = 0.15

#Calculo de z3
z3 = (h1*w7) + (h2*w8) + Y
print("Suma ponderada de la capa de salida (z3):", round(z3, 4)) 


# Función de activación sigmoide
def sigmoid(z):
    return 1 / (1 + math.exp(-z))

# Llamamos la función de activación de la capa de salida
output = sigmoid(z3)
print("Salida de la red neuronal:", round(output, 4))