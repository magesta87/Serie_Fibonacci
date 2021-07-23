#*****************SERIE FIBONACCI***************
#*El primer elemento de la secuencia es igual a uno (Fib1 = 1).
#El segundo elemento también es igual a uno (Fib2 = 1).
#Cada numero después de ellos son la suman de los dos números anteriores (Fibi = Fibi-1 + Fibi-2).

def fib(n):
    if n < 1:
         return None
    if n < 3:
        return 1

    elem1 = elem2 = 1
    sum = 0
    for i in range(3, n + 1):
        sum = elem1 + elem2
        elem1, elem2 = elem2, sum
    return sum

for n in range(1, 10): # probando
    print(n, "->", fib(n))


#***************VERSION CORTA DE FIBONACCI******************

def fib(n):
    if n < 0:
        return None
    if n < 3:
        return 1
        
    return fib(n - 1) + fib(n - 2)


#BUCLE DE PRUEBA
for i in range(20):    
    print(i, "->",fib(i))
