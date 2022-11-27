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



"""2. Design a method called isLeapYear that receives a number and returns False for
common years and True for leap years. You may know that a year is considered to
be a leap year if it is divisible by 4, unless it is also divisible by 100. A year is not a
leap year if it is divisible by 100 unless it is also divisible by 400."""

number=2012

def isLeapYear (number):
    year=None
    if (number%4==0 and number%100!=0) or (number%100==0 and number%400==0):
        year=False 
    else:
        year
    return year
print(isLeapYear(number))


"""3. Diseñe un método llamado ComputeDaysInMonth que devuelva el número de días para el
 mes y el año que se reciben como argumentos. Puede usar el método bisiesto anterior.
 Si los valores no son válidos, el método debería devolver -1."""

mes=11
año=2022
def ComputeDaysInMonth (mes, año):
    diasTotal=0
    meses=[31,28,31,30,31,30,31,31,30,31,30,31]
    if mes>12 or mes<1 or año<1:
        diasTotal=-1
    else:
        if isLeapYear(number)==False and mes==2:
            diasTotal=29
        else:
            diasTotal=meses[mes-1]
    return diasTotal
print(ComputeDaysInMonth(mes, año))


"""4."""
day=4
month=15
year=2005

def getDayOfWeek (day, month, year):
    DaysWeek={0:"Domingo", 1:"Lunes", 2:"Martes", 3:"Miércoles",
               4:"Jueves", 5:"Viernes", 6:"Sábado"}
    #DaysMonth=[31,28,31,30,31,30,31,31,30,31,30,31]
    
    if month<1 or year<1 or day>31:
        print("Error")
    else:
        a = (14 - month) // 12
        y = year - a
        m = month + 12 * a - 2
        d = int(((day + y + y//4 - y//100 + y//400 + (31*m)//12) % 7))
        d = DaysWeek[d]
    return d
print(getDayOfWeek(day, month, year))


"""5"""


