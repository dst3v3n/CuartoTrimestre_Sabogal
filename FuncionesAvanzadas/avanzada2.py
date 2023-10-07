def base(x):                        # Se crea una funcion llamada "base" que tiene un parametro de nombre "x"
    def suma(y):                    # Se crea una funcion dentro de la funcion "base" llamada "suma" que tiene un parametro de nombre "y"
        return x+y                  # Retorna el valor de la operacion x + y. "x" proviene de la funcion "base" y "y" de la funcion "suma"
        #print(x+y)                 # imprime el valor de la operacion x + y. "x" proviene de la funcion "base" y "y" de la funcion "suma"

    def resta(y):                   # Se crea una funcion dentro de la funcion "base" llamada "resta" que tiene un parametro de nombre "y"
        return x-y                  # Retorna el valor de la operacion x - y. "x" proviene de la funcion "base" y "y" de la funcion "suma"
    
    return [suma,resta]             # Retorna una lista que tiene dos valores que son las funciones que estan dentro de la funcion "base"

usoFuncionRetornada=base(10)        # define una variable llamada "usoFuncionRetornada" en el cual le asignan la funcion "base" se le asigna como argumento el numero 10
print(usoFuncionRetornada[1](20))   # Se imprime la funcion "usoFuncionRetornada" mediante los corchetes "[]" podemos asignarle el indice de la funcion que tiene la funcion "base"
                                    # Ya definido la funcion interna que quiere usar, ponemos el argumento de la funcion seleccionada.
                                    # En este caso se selecciono la funcion resta, se le asigna como argumento de la funcion el numero 20