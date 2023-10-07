def base(funcion):                  # crea una funcion llamada "base" que tiene un parametro con el nombre de "funcion"
    def interna(n1,n2):             # crea una funcion interna que se llama "interna" que tiene dos parametros "n1" y "n2" 
        #print(funcion(n1,n2))#*    # imprime la funcion que asigno en el parametro de la funcion "base", la funcion asignada tiene como parametros la funcion "n1" y "n2"
        return funcion(n1,n2)       # retorna la funcion que asigno en el parametro de la funcion "base", la funcion asignada tiene como parametros la funcion "n1" y "n2"
    return interna                  # retorna la funcion interna

def suma(num1,num2):                # crea una funcion llamada "suma" que tiene dos parametros "num1" y "num2"
    return num1+num2                # Retorna el resultado de la operacion n1 + n2

def resta(num1,num2):               # crea una funcion llamada "resta" que tiene dos parametros "num1" y "num2"
    return num1-num2                # Retorna el resultado de la operacion n1 - n2

var1=base(suma)                     # define una variable llamada var1, tiene como argumento posicional el nombre de la funcion "suma"
var2=base(resta)                    # define una variable llamada var1, tiene como argumento posicional el nombre de la funcion "resta"
#var1(10,15)#*                      # llama la funcion var1 y tiene como argumentos posicionales "10" , "15"
#var2(15,10)#*                      # llama la funcion var2 y tiene como argumentos posicionales "15" , "10"
print(var1(10,15))                  # imprime la funcion var1 y tiene como argumentos posicionales "10" , "15"
print(var2(15,10))                  # imprime la funcion var2 y tiene como argumentos posicionales "15" , "10"