# def suma(num1,num2):
#     return num1+num2
#     #print(num1+num2)

def suma(*args):                            # Se crea una funcion con el nombre de "suma", que tiene un parametro especial llamado "args"
    print(type(args))                       # Se imprime el typo de dato que tiene el parametro args, que es un parametro especial

def mayor(*args):                           # Se crea una funcion con el nombre de "mayor", que tiene un parametro especial llamado "args"
    m=0                                     # Se declara una variable llamada "m" que se le asigno un valor de tipo entero que es un "0"
    for i in args:                          # Se usa el bucle for para iterar los valores del parametro especial "args", que es una tupla
        if i>m:                             # Se crea una condicion que evalua si i es mayor a m
            m=i                             # Si se cumple esa condicion la variable m se le asigna el valor que tiene i
    return m                                # Se le retorna la variable m

print(mayor(10,23,21,100,1000,1,2,3))       # Llama la funcion "mayor" y le da como argumentos varios valores de tipo entero
                                            # Usa la funcion print que imprime por pantalla el valor que va a retornar la funcion "mayor"

#suma(10,23,21)
#suma('hola',122,[],{})