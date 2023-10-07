# Crea una función llamada calcular_precio_total que acepte varios argumentos de palabra clave que representen productos y sus precios. 
# La función debe calcular y devolver el precio total de la compra. Además, debe permitir aplicar descuentos opcionales a algunos de los productos.

def calcular_precio_total (*args , **kwargs):
    suma = 0
    tupla = ()
    for key , value in kwargs.items():
        suma += value
    print(suma)

    for i in args:
        descuento = suma*(i / 100)
    
    print(descuento)
              

calcular_precio_total (50 , 70, banano=1500 , fresa=2000)