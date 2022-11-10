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
    lista[0]=sustituto
    return lista
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


def desplazar(lista):
    numAntiguo=lista[0]
    numCambio=0
    lista[0]=lista[(len(lista))-1]
    for i in range(1,len(lista)):
        numCambio=lista[i]
        lista[i]=numAntiguo
        numAntiguo=numCambio
    
    return lista
print(desplazar(lista))
    


"""3. Realiza un programa que solicite la fecha como tres datos numéricos (día, mes y
año) y muestre a continuación la fecha en formato largo.
Introduce el día de la fecha: 15
Introduce el mes de a fecha: 3
Introduce el año de a fecha: 2009
La fecha en formato largo es 15 de Marzo de 2009
Debe validar los datos y ejecutarse hasta que se introduzca un día negativo."""

def solicitarFecha(dia, mes, anno):
    mensaje=f"La fecha en formato largo es {dia} de {mes} de {anno}"
    return mensaje

dia=int(input("dia: "))
mes=int(input("mes: "))
anno=int(input("anno: "))
while dia >0:
    while dia <1 and dia >31:
        dia=int(input(". error. dia: "))
    mes=int(input("mes: "))
    while mes not in ["1", "2", "3", "4", "5", "6", "7", "8","9", "10", "11", "12"]:
        mes=int(input("error. mes: "))
    anno=int(input("anno: "))
    while anno <0:
        anno=int(input("error. anno: "))
    print(solicitarFecha(dia, mes, anno))
    dia=int(input("dia: "))
    mes=int(input("mes: "))
    anno=int(input("anno: "))
    print(solicitarFecha(dia, mes, anno))
        
print(solicitarFecha(dia, mes, anno))
        
        
"""4"""

num=int(input("introduce un numero: "))

lista= []
pares=[]
mayor=0

while num>=0:
    lista.append(num)
    #if num>mayor:
    #    mayor=num
    if num%2==0:
        pares.append(num)
    num=int(input("introduce un numero: "))
#print(f"Programa finalizado. El número mayor de la lista es {mayor} ")
print("El mayor de la lista es ", (obtenerMayor(lista)))
print("Los pares son", pares)

"""for i in range(len(lista)):
    if i%2=0:
        pares.append(i)
print(pares)"""
        
        
"""5. Realiza una función reverse que reciba una lista y devuelva una nueva lista cuyo
contenido sea igual a la original pero invertida. Así, dada la lista [‘Di’, ‘buen’, ‘día’, ‘a’,
‘papa’], deberá devolver [‘papa’, ‘a’, ‘día’, ‘buen’, ‘Di’]."""



lista=["Di", "buen", "día", "a", "papa"]

def reversed(lista):
for i in reversed(systems):
    return i

print(list(reversed(["Di", "buen", "día", "a", "papa"])))



"""6"""

lista=[0,4,3,1,5,2]

for
if num>mayor:
    mayor=num
    if num%2==0:
        pares.append(num)
    num=int(input("introduce un numero: "))
#print(f"Programa finalizado. El número mayor de la lista es {mayor} ")
print("El mayor de la lista es ", (obtenerMayor(lista)))
print("Los pares son", pares)

