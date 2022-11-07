'''
Created on 7 nov 2022

@author: Admin
'''
from random import randint

lista=[]

for i in range(100):
    lista.append(randint(0,100))
    
#print(lista)

def obtenerMayor(lista):
    mayor= lista[0]
    for i in range(len(lista)):
        if lista[i] > mayor:
            mayor=lista[i]
    return mayor


print(lista)
print(obtenerMayor(lista))

print("Ha terminado")

def obtenerMenor (lista):
    menor= lista[0]
    for i in range(len(lista)):
        if lista[i] < menor:
            menor=lista[i]
    return menor


print(lista)
print(obtenerMenor(lista))

def sumar (lista):
    suma=0
    for i in range(len(lista)):
        suma+=i
    return suma
print(lista)
print(sumar(lista))



def mediaa (lista):
    media=lista[0]
    for i in range(len(lista)):
        media=sumar(lista)/len(lista)
    return media
print(lista)
print(mediaa(lista))

sustituto=int(input("introduce un numero: "))
def sustituir (lista):
    for i in range(len(lista)):
        lista[10]=sustituto
    return sustituto
print(sustituir(lista))
print(lista)


def mostrar (lista):
    numeros=lista[0]
    for i in range(len(lista)):
        numeros=lista
    return numeros
print(mostrar(lista))


"""2. Realiza un programa que lea 10 números, los imprima separados por coma y a
continuación los desplace una posición (y los muestre por pantalla desplazados), de
tal forma que el último pase a la primera posición, el primero a la segunda, el
segundo a la tercera, y así sucesivamente."""

lista=[1,2,3,4,5,6,7,8,9,10]

for i in range(len(lista)):
    lista[i]+
    


"""3. Realiza un programa que solicite la fecha como tres datos numéricos (día, mes y
año) y muestre a continuación la fecha en formato largo.
Introduce el día de la fecha: 15
Introduce el mes de a fecha: 3
Introduce el año de a fecha: 2009
La fecha en formato largo es 15 de Marzo de 2009
Debe validar los datos y ejecutarse hasta que se introduzca un día negativo."""


        
        