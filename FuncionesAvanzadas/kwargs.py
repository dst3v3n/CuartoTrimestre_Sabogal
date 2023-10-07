def function(**kwargs):                                 # Crea una funcion llamada "funtion" que tiene un parametro especial llamado "kwargs"
    #print(type(kwargs))                                # Usa dos funciona, una es el "Type" que se usa para saber la clase que pertenece el valor que asignamos a la funcion que en este caso es "kwargs"
                                                        # la otra es "Print" que se usa para imprimir por pantalla lo que queremos mostrar, en este caso lo que retorna la funcion "Type"
    for key in kwargs.keys():                           # Usa el bucle "for" para iterar los valores del parametro especial "kwargs" con el metodo "key()", este metodo es de un diccionario y solo va a iterar las claves del diccionario
        print(key)                                      # Va a imprimir por pantalla el valor que tiene "key" en cada iteracion

    for value in kwargs.values():                       # Usa el bucle "for" para iterar los valores del parametro especial "kwargs" con el metodo "values()", este metodo es de un diccionario y solo va a iterar los valores del diccionario
        print(value)                                    # Va a imprimir por pantalla el valor que tiene "value" en cada iteracion

    for key,value in kwargs.items():                    # Usa el bucle "for" para iterar los valores del parametro especial "kwargs" con el metodo "items()", este metodo es de un diccionario y va a iterar las claves y los valores del diccionario
        print(f'{key} : {value}')                       # Va a imprimir por pantalla las variables "key" y "value" mediante un formato especifico


function(programa="adso",ficha=2693629,aprendices=16)   # Llama la funcion "function" y le da como argumentos varios valores, deben contener una estructura definida por el tipo de parametro que definimos en la funcion
                                                        # La estructura es "Nombre de la clave (que sea un string) "=" El valor"