'''
Created on 1 dic 2022

@author: Admin
'''
#dni="29542865D"
#dni="43569745V"
dni="3759375W"
#dni="5862745E"
def comprobarDNI (dni):
    letras=["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E"]
    dniValido=False
    cifras=dni[0:-1]
    resto=int(cifras)%23
    letra=letras[resto]
   
    if (len(dni)<=9 or len(dni)>=8) and dni[-1] in letras:
        if dni==str(cifras)+str(letra):
            dniValido=True
    
    return dniValido

assert(comprobarDNI("29542865D")==True)
assert(comprobarDNI("43569745V")==True)
assert(comprobarDNI("3759375W")==True)
assert(comprobarDNI("5862745E")==True)

print(comprobarDNI(dni))