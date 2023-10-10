# CuartoTrimestre_Sabogal

[![Python](https://img.shields.io/badge/Python-1.11.3+-F23545?style=for-the-badge&logo=python&logoColor=F23545&labelColor=black)](https://www.python.org/)
[![django](https://img.shields.io/badge/django-4.2+-F23545?style=for-the-badge&logo=django&logoColor=F23545&labelColor=black)](https://www.djangoproject.com/)
[![mongo](https://img.shields.io/badge/mongodb-1.40.2+-F23545?style=for-the-badge&logo=mongodb&logoColor=F23545&labelColor=black)](https://www.mongodb.com/es)


> Contenido del curso
* [Funciones Avanzadas](./FuncionesAvanzadas/)

---
## **Ultimos codigos realizados**

```python
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

```
> El codigo lo encuentra **[Aqui](./FuncionesAvanzadas/ejercicio_avanzada.py)**

### Hola, mi nombre es Steven Sabogal.


Soy estudiante del SENA desde hace dos año. Este años estoy aprendiendo sobre Analisis y Desarrollo de Software (ADSO). Quiero seguir aprendiendo mas sobre el mundo del Desarrollo de software **[@dst3v3n](https://github.com/dst3v3n)**.

### En mi perfil de GitHub tienes más información

[![Web](https://img.shields.io/badge/Guthub-dst3v3n-F23545?style=for-the-badge&logo=github&logoColor=F23545&labelColor=black)](https://github.com/dst3v3n)