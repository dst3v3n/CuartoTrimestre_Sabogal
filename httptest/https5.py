import requests
import json
url="https://httpbin.org/post"#?nombre=juan&documento=12345"
argumentos={
    'nombre':'Juan',
    'documento':'12345'
}

theheaders={
    'Content-Type':'Text',
    'access-token':'12345'
}

response=requests.post(url,json=json.dumps(argumentos),headers=theheaders)
decodetest=response.content.decode()
print('*'*20)
print(decodetest)

url="https://httpbin.org/delete"
response = requests.delete(url)
print(response.status_code.decode())
print(response.content)

url="https://httpbin.org/put"
response = requests.put(url)
print(response.status_code.decode())
print(response.content)