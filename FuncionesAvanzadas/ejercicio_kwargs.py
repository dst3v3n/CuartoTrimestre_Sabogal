def valores (**kwargs):
    for values in kwargs.values():
        print(values)

def ClaveValores (**kwargs):
    print(kwargs)
    for key,values in kwargs.items():
        print(f"{key} : {values}")
        
valores (programa="adso" , ficha=2693629 , aprendices=16)
print("")
ClaveValores (programa="adso" , ficha=2693629 , aprendices=16)