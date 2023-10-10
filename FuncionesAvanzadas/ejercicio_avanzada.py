# Crea un decorador que verifique si un usuario está autenticado antes de ejecutar una función. 
# Puedes simular la autenticación con un diccionario que contenga nombres de usuario y contraseñas.

user = input("Digita tu usuario ")
password = input("Digita tu contraseña ")

db = {
    "harold" : "haroldsabogal",
    "steven" : "steven",
    "josue" : "aureliocasillas",
    "sebastian" : "sebastian"
}

def base (funcion):
    def validar (usuario:str , contraseña:str):
        user , psswd = validacion(usuario , contraseña)
        if user == True and psswd == True:
            funcion()
    return validar

@base
def bienvenida ():
    print("Bienvenido")

def validacion (usuario:str , contraseña:str):
    # Usuario
    if usuario in db:
        usr = True
    else:
        usr = False
    
    # Contraseña
    if db[usuario] == contraseña:
        pssw =  True
    else:
        pssw = False

    return [usr , pssw]

bienvenida (user , password)