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

def estaOrdenada (lista):
    valida=True
    for i in range(1,len(lista)):
        if lista[i]<lista[i-1]:
            return False 
    return valida
print(estaOrdenada(lista))


"""7.Escribir una función denominada encajan que indique si dos fichas de dominó
encajan o no. Las fichas son recibidas en dos cadenas de texto con el siguiente
formato
[3,4] [2,5]"""
ficha1=[3,4]
ficha2=[2,5]

def encaja(ficha1,ficha2):
    encaja=True 
    if ficha1[0]==ficha2[0]:
        encaja=True 
    elif ficha1[1]==ficha2[1]:
        encaja=True 
    elif ficha1[1]==ficha2[0]:
        encaja=True 
    elif ficha1[0]==ficha2[1]:
        encaja=True    
    return encaja 
print(encaja(ficha1, ficha2))


"""8"""

lista=[]
num=0
while num>=0:
    num=int(input("introduce numero: "))
    if num>0:
        lista.append(num)
print(lista)

def num_primos (lista):  
    num_primos=[]
    for i in range (len(lista)):
        contador=0
        num=lista[i]
        for i in range (2, num):
            if num%i==0:
                contador+=1
        if contador==0:
            num_primos.append(num)       
    return (num_primos)  

print (f"En la lista son número primos {num_primos (lista)}")


def sumar (lista):
    suma=0
    for i in (lista):
        suma+=i
    return suma
print(sumar(lista))    
print (f"La suma de los elementos de la lista es {sumar(lista)}")

def media (lista):
    media=sumar(lista)/(len(lista))
    return (media)
print (f"La media de la lista es {media(lista)}")


def factorial(lista):
    lista_factoriales=[]
    return factorizado
    factorial=1
    while num>0:
        for i in lista:
            for j in range (i, 1, -1):
                factorial=factorial*j
            lista_factoriales+=[factorial]
    return lista_factoriales
print (f"Los factoriales de cada elemento de la lista, en orden, son {factorial(lista)}")


"""9. Desarrolla un programa que a partir de una lista de números y un entero k, realice la
llamada a tres funciones: a) para devolver una lista de números con los menores de
k, b) otra con los mayores y c) otra con aquellos que son múltiplos de k."""


lista=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
numero=9

def obtenerMenorQue (lista):
  listaMenoresQue=[]
  for i in range(len(lista)):
    if lista[i] < numero:
      listaMenoresQue.append(lista[i])
          
  return listaMenoresQue

print(obtenerMenorQue(lista))

def obtenerMayorQue (lista):
  listaMayoresQue=[]
  for i in range(len(lista)):
    if lista[i] > numero:
      listaMayoresQue.append(lista[i])
          
  return listaMayoresQue

print(obtenerMayorQue(lista))


def es_multiplo(lista):
    listaMultiplos=[]
    for i in range(len(lista)):
        if lista[i] % numero == 0:
            listaMultiplos.append(lista[i])
    return listaMultiplos
print(es_multiplo(lista))



"""11. Escribe una función intersect que reciba dos listas y devuelva otra lista con los
elementos que son comunes a ambas, sin repetir ninguno."""

lista=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]

lista2=[2,4,5,8,10,15,30,20,25,90,7]

def intersect(lista, lista2):
    listaComunes=[]
    for i in lista:
           if i in lista2 and i not in listaComunes:
               listaComunes.append(i)
    return listaComunes
print(intersect(lista, lista2))



"""12. Escribe una función unionListas que reciba dos listas y devuelva los elementos que
pertenecen a una, o bien, a la otra, pero sin repetir ninguno (unión de conjuntos)."""

lista=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]

lista2=[2,4,5,8,10,15,30,20,25,90,7]

def unionListas (lista,lista2):
    Comun=[]
    for i in lista:
        if i in lista:
            Comun.append(i)
    for j in lista2:
        if j in lista2 and j not in lista:
            Comun.append(j)
    return Comun
print(unionListas (lista,lista2))


"""13. Escribe una función que, dada una lista de nombres y una letra, devuelva una lista
con todos los nombres que empiezan por dicha letra. Debe validar los datos."""

lista=["Manuel", "Horacio", "Homero", "Pepe", "Antonio", "Luis"]

letra="H"

def DevolverNombres (lista, letra):
    listaNombres=[]
    for i in lista:
        if i[0]==letra:
            listaNombres.append(i)
    return listaNombres
print(DevolverNombres (lista, letra))
            


            
"""14. Escribe una función que, dada una lista de cadenas, devuelva la cadena más larga.
Si dos o más cadenas miden lo mismo y son las más largas, la función devolverá la
que tenga el mayor número de caracteres repetidos."""

lista=["Gol", "Hola", "Uno", "Cabeza", "No", "Lalala"]

def devolverCadenaLarga (lista):
    cadenaMayor=""
    caracteres=[0]
    comparado=[]
    for cadena in lista:
        if len(cadena)>len(cadenaMayor): 
            cadenaMayor=cadena
        if len(cadena)==len(cadenaMayor):           
    for cadena in lista:
        if len(cadenaMayor) == len(i):
            comparado.append(i)
    for j in comparado:
        if i==

    
    





print(devolverCadenaLarga(lista))
            
