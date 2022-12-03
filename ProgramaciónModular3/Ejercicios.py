'''A
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


"""4. Diseñe una función llamada númeroEnCadena que reciba una cadena de caracteres como parámetro
 y devuelva cuántos de ellos son números."""
 
cadena="hd73hd83hd93hd93hd93hd9"
 
def numeroenCadena (cadena):
    numeros=0
    for i in cadena:
        if i.isdigit():
            numeros+=1
    return numeros
print(numeroenCadena(cadena))
     

"""5. Diseñar una función llamada palíndromo que tenga como parámetro de entrada una cadena de caracteres, y devuelva
 True si es un palíndromo o False en los demás casos. Una palabra es un palíndromo si se puede leer igual de 
 izquierda a derecha o de derecha a izquierda, ignorando los blancos. Por ejemplo: "anilina" o "Dabale arroz a 
 la zorra el abad" Para simplificar el problema, se puede suponer que se utilizan caracteres simples, es decir, sin 
 tildes ni diresis."""
 
cadena="Dabale arroz a la zorra el abad"
def palindromo (cadena):
    cadena = cadena.replace(" ", "")
    palindromomo=False 
    if cadena.lower()==cadena[::-1].lower():
        palindromomo=True 
    return palindromomo
print(palindromo(cadena))


"""6.Realizar una función que busque una palabra escondida dentro de un texto. Por ejemplo,si la cadena es
 “shybaoxlna” y la palabra que queremos buscar es “hola”, entonces si seencontrará y deberá devolver True, en
  caso contrario deberá devolver False. Las letrasde la palabra escondida deben aparecer en el orden correcto en 
  la cadena que la oculta:
          shybaoxlna ⇒ hola: True
          soybahxlna ⇒ hola: False"""


cadena="shybaoxlna"
palabraBusca="hola"

def buscarPalabra (cadena, palabraBusca):
    palabra=""
    contador=0
    valido=False
    for i in cadena:
        if i==palabraBusca[contador]:
            palabra+=i
            contador+=1
    if palabra==palabraBusca:
        valido=True
    return valido
print(buscarPalabra(cadena, palabraBusca))
        
        
        
"""7. Diseñar una función que reciba como parámetro tres cadenas, la primera será una frase y deberá buscar
 si existe la palabra que recibe como segundo parámetro y reemplazarlapor la tercera."""
 
cadena="Hola, Manuel"
palabraBusca="Manuel"
palabra2="Pepe"

def cambiarPalabra (cadena, palabraBusca, palabra2):
    resultado=""
    if buscarPalabra(cadena, palabraBusca)==True:
        palabraBusca=palabra2
        #borrar palabraBusca en cadena
        resultado=cadena+palabra2
    return resultado
print(cambiarPalabra(cadena, palabraBusca, palabra2))


"""8.Diseñar una función que determine la cantidad de vocales diferentes, que tiene una palabra o frase 
introducida por teclado. Por ejemplo, la cadena “Abaco”, devolvería 2."""

cadena="Buenas tardes, Pepe"

def contarVocales (cadena):
    vocales="aeiou"
    vocalesEncontradas=[]
    for i in cadena:
        if i in vocales:
            if i not in vocalesEncontradas:
                vocalesEncontradas.append(i)
    return len(vocalesEncontradas)
print(contarVocales(cadena))
            
                
            
""".9. 9. Crear una función que, tomando una cadena de texto como entrada, construya y devuelva 
otra cadena formada de la siguiente manera: todas las consonantes estarán al principio y todas las 
vocales al final de la misma, eliminando los blancos. Por ejemplo,pasándole la cadena "curso de programacion", una 
posible solución sería"crsdprgrmcnuoeoaaio’."""

cadena="El plato se ha roto."

def ConsonantesYVocales (cadena):
    vocales="aeiou"
    consonantes="qwrtypsdfghjklñzxcvbnm"
    resultado=""
    for j in cadena.lower():
        if j in consonantes:
            resultado+=j

    for i in cadena.lower():
        if i in vocales:
            resultado+=i

            
    return resultado
print(ConsonantesYVocales(cadena))


"""10. Escribir una función que devuelva el número de palabras que hay en una cadena que recibe como parámetro. 
Ten en cuenta que entre dos palabras puede haber más de un blanco. También al principio y al final de la frase puede
haber blancos redundantes. Por ejemplo, si la cadena es “He estudiado mucho”, debe devolver 3."""
 
cadena=" El balón  se ha desinflado "

def numeroPalabras (cadena):
    resultado=[]
    for i in cadena:
        if i 
#No sé
