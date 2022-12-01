'''
Created on Nov 29, 2022

@author: estudiante
'''
"""1.Diseñe una función llamada caracteresEnCadena que tenga una cadena
 de caracteres y un carácter como parámetros de entrada y devuelva cuántas
  veces aparece ese carácter en la cadena. Debería hacerlo sin importar 
  si la cadena y el carácter son minúsculas o mayúsculas.."""

cadena="HolaPepe".upper()
caracter="P".upper()

def charactersInString (cadena, caracter):
    contador=0
    for i in cadena.upper:
        if i==caracter.upper():
            contador+=1
    return contador
print(charactersInString (cadena, caracter))
    
    
    
"""2. 2. Diseñe una función llamada lowCaseInString que tenga una cadena 
de caracteres como parámetro, el método debe devolver cuántos de esos 
caracteres son letras minúsculas."""


cadena="Messi"

def lowCaseInString (cadena):
    contador=0
    for i in cadena:
        if (i.islower()):
            contador+=1
    return contador
print(lowCaseInString (cadena))



"""3.3. Design a function called upperCaseInString that has a string of
characters as parameter and the method should return how many are uppercase 
letters."""
cadena="HolaJe"
def uppercaseletters (cadena):
    contador=0
    for i in cadena:
        if (i.isupper()):
            contador+=1
    return contador
print(uppercaseletters (cadena))


def uppercaseletters (cadena):
    contador=0
    for i in cadena:
        if i.upper==caracter.upper:
            contador+=1
    return contador
print(uppercaseletters (cadena))

    