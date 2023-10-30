import requests
url='http://gutendex.com/books/'
response=requests.get(url)
diccionario=response.json()
#print(type(diccionario))
resultados=diccionario['results']
print(type(resultados))
print(len(resultados))
print(type(resultados[0]))
#print(resultados[0])
titulos = []
for libro in resultados:
    for key, value in libro.items():
        if key == "title":
            titulos.append(value) 
            print(f'{key} : {value}')

titulos.sort()
for i in titulos:
    print(i)