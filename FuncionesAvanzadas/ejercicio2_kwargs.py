# edad = int(input("Digita tu edad"))
edad1 = input("Digita tu edad: ")                           # Declara una variable que se llama "edad1", se le asigna la funcion "input", se usa para que digiten un valor por pantalla
peso1 = input("Digita tu peso: ")                           # Declara una variable que se llama "peso1", se le asigna la funcion "input", se usa para que digiten un valor por pantalla
estatura1 = input("Digita tu estatura: ")                   # Declara una variable que se llama "estatura1", se le asigna la funcion "input" se usa para que digiten un valor por pantalla

def validacion (**kwargs):                                  # Se crea una funcion llamada "validacion" que tiene un parametro especial llamado "kwargs"
    for key,value in kwargs.items():                        # Usa el bucle "for" para iterar los valores del parametro especial "kwargs" con el metodo "items()", este metodo es de un diccionario y va a iterar las claves y los valores del diccionario
        try:                                                # Usa la palabra try que se usa para el manejo de "Except"

            if key == "edad":                               # Se crea una condicion que evalua si la variable "key" es igual a "edad"
                value = int(value)                          # Se define una variable llamada "value" y se le asigna la funcion "int" que convierte el valor que se le asigne a la al tipo de dato entero
                verdadero = isinstance(value,int)           # Se define una variable llamada "verdadero", se le asigna la funcion "isinstance" que comprueba si un objeto es una instancia de un tipo de dato
                print(verdadero)                            # Imprime el valor que contiene la variable "verdadero"
                if verdadero == False:                      # Se crea una condicion que evalua si la variable "Verdadero" es igual a "False"
                    raise ValueError                        # Si se cumple la condicion se usa la palabra clave "raise" para forzar a que de un error de tipo "ValueError"
                
            if key == "peso":                               # Se crea una condicion que evalua si la variable "key" es igual a "peso"
                for h in value:                             # Se usa el bucle "for" para iterar los valores de la variable "value"
                    if h == ".":                            # Se crea una condicion que evalua si la variable "h" es igual a "." 
                        value = float(value)                # Se define una variable llamada "value" y se le asigna la funcion "int" que convierte el valor que se le asigne a la al tipo de dato real
                        print(isinstance(value,float))      # se imprime la funcion "isinstance" que comprueba si un objeto es una instancia de un tipo de dato
                    else:                                   # si no se cumple la condicion
                        raise ValueError                    # se usa la palabra clave "raise" para forzar a que de un error de tipo "ValueError"
                    
            if key == "estatura":                           # Se crea una condicion que evalua si la variable "key" es igual a "estatura"
                for h in value:                             # Se usa el bucle "for" para iterar los valores de la variable "value"
                    if h == ".":                            # Se crea una condicion que evalua si la variable "h" es igual a "." 
                        value = float(value)                # Se define una variable llamada "value" y se le asigna la funcion "int" que convierte el valor que se le asigne a la al tipo de dato real
                        print(isinstance(value,float))      # se imprime la funcion "isinstance" que comprueba si un objeto es una instancia de un tipo de dato
                    else:                                   # si no se cumple la condicion
                        raise ValueError                    # se usa la palabra clave "raise" para forzar a que de un error de tipo "ValueError"
                    
        except:                                             # Usa la palabra "except" para manejar los errores que pueden suceder en el bloque de codigo de la palabra reservada "try"
            print("No es el valor esperado")                # Si se genera un error en el bloque de codigo de "try", imprimira por pantalla lo que esta dentro de la funcion "print"
            
validacion(edad=edad1 , peso=peso1 , estatura=estatura1 )   # Se llama la funcion "validacion" y le da como argumento 3 valores que son clave valor ya que definimos en la funcion el parametro especial "kwargs"
                                                            # Lo que permite ese parametro es guardar los argumentos en un diccionari. Significa que la parte que esta al lado izquierdo del igual es clave
                                                            # y lo que esta a la derecha es el valor