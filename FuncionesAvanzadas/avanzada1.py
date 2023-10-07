def suma(n1,n2):                            # Se crea una funcion llamada "suma" que tiene dos parametros "n1" y "n2"
    return n1+n2                            # Retorna el valor de la operacion n1 + n2

def resta(n1,n2):                           # Se crea una funcion llamada "resta" que tiene dos parametros "n1" y "n2"
    return n1-n2                            # Retorna el valor de la operacion n1 - n2

def producto(n1,n2):                        # Se crea una funcion llamada "producto" que tiene dos parametros "n1" y "n2"
    return n1*n2                            # Retorna el valor de la operacion n1 * n2

def division(n1,n2):                        # Se crea una funcion llamada "division" que tiene dos parametros "n1" y "n2"
    return n1/n2                            # Retorna el valor de la operacion n1 / n2

def operacion(funcion,numero1,numero2):     # Se crea una funcion llamada "operacion" que tiene tres parametros "funcion" , "numero1" y "numero2"
    print(funcion(numero1,numero2))         # se imprime la funcion "funcion" que es el argumento del parametro "operacion". 
                                            # los artibutos del argumento "funcion" son los atributos de la funcion "operacion" es decir "numero1" y "numero2"

operacion(suma,10,5)                        # Se llama la funcion "operacion" con los argumentos posicionales "funcion" = suma , "numero1" = 10 ,  "numero2" = 5