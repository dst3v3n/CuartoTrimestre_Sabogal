# Escriba una funcion que imprima la suma de numeros y el promedio de una serie de numeros independientes

def SumaPromedio (*args):
    suma = 0
    for i in args:
        suma += i
    
    print(suma)
    print(suma / len(args))

SumaPromedio (10 , 20 , 50 , 70 , 100 , 150)