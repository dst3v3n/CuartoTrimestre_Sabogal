import random

def llenarlista ():
    lista = [random.randint(10,50) for i in range(random.randrange(10,25))]
    return lista

def sumar():
    lista = llenarlista()
    suma = 0
    for i in lista:
        suma += i
    print(lista)
    return suma

def mayor():
    lista = llenarlista()
    mayor = 0
    for i in lista:
        if i>mayor:
            mayor = i
    print(lista)
    return mayor

def menor():
    lista = llenarlista()
    menor = 1000000000000
    for i in lista:
        if i<menor:
            menor = i
    print(lista)
    return menor

def operacion (funcion):
    return funcion()

print (operacion(sumar))

print("")
print (operacion(mayor))
print("")
print (operacion(menor))
print("")
print (operacion(llenarlista))