def base(funcion):                      # crea una funcion llamada "base" que tiene un parametro con el nombre de "funcion"
    print('Inicia la función base')     # imprime por pantalla "Inicia la funcion base"
    def interna():                      # Crea una funcion llamada "interna" no tiene parametros. La funcion "interna" esta dentro de la funcion "base"
        funcion()                       # Ejecuta la funcion que optamos por usar en el parametro de la funcion "base"
    print('Finaliza la función base')   # imprime por pantalla "Finaliza la funcion base"
    return interna                      # Retorna la funcion(interna)

def integrada():                        # crea una funcion llamada "integrada" no tiene parametros
    print('Funcion Integrada')          # imprime por pantalla "Funcion Integrada"

def otraFuncion():                      # crea una funcion llamada "otraFuncion" no tiene parametros
    print('Otra Funcion')               # Imprime por pantalla "Otra Funcion"

var1=base(integrada)                    # Definimos una variable llamada var1 y le asignamos la funcion "base", le ponemos como argumento una funcion externa, en este caso le asignamos la funcion "integrada"
var2=base(otraFuncion)                  # Definimos una variable llamada var2 y le asignamos la funcion "base", le ponemos como argumento una funcion externa, en este caso le asignamos la funcion "otraFuncion"
var1()                                  # llamamos la funcion "var1" sin argumentos
var2()                                  # llamamos la funcion "var2" sin argumentos