def funcion(*args,**kwargs):                        # Se crea una funcion con el nombre de "funcion", que tiene dos parametros especiales llamados "args" y "kwargs"
    for elemento in args:                           # Se usa el bucle "for" para iterar los valores que contiene el parametro "args"
        print(elemento)                             # Usa la funcion "print" para que imprima el valor que contiene la variable "elemento" en cada iteracion
    
    for key,val in kwargs.items():                  # Usa el bucle "for" para iterar los valores del parametro especial "kwargs" con el metodo "items()", este metodo es de un diccionario y va a iterar las claves y los valores del diccionario
        print(f'{key} : {val}')                     # Va a imprimir por pantalla las variables "key" y "value" mediante un formato especifico

funcion(1,2,3,4, fecha='6-10-2023',hora='7:30 am')  # Llama a la funcion "funcion" que contiene varios argumentos de especificamente 6 valores, cuatro argumentos es para el parametro especial "args" y "kwargs"
                                                    # *Args* el paramtro permite introducir valores infinitos y son guardados en una tupla
                                                    # *Kwargs* el paramtro permite introducir valores infinitos y son gurdados en un diccionario, tiene una sintaxis definida. 
                                                    # La sintaxis es la siguiente "Nombre de la clave (que sea un string) "=" El valor"

x=100                                               # Se declara una variable llamada "x" que se le asigno un valor de tipo entero que es un "100"
print(isinstance(x,int))                            # se imprime la funcion "isinstance" que comprueba si un objeto es una instancia de un tipo de dato