'''
Created on Nov 22, 2022

@author: estudiante
'''

"""1."""
numero=4
def factorial(numero):
    factorial=1
    for j in range(1,numero+1):
            factorial=factorial*j
    return factorial
print(factorial(numero))
