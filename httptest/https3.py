import requests
import json

import requests
import json

url="https://httpbin.org/get"#?nombre=juan&documento=12345"
response=requests.get(url)
#print(response.content.decode())
decodetest=response.content.decode()
print(type(decodetest))
print(response.json())
print('*'*20)
decodetestjson=json.loads(response.content)
print(decodetestjson)
print('*'*20)
print(decodetest)

# print(response.content.decode())
# print(type(response.content.decode()))
# jsonresponse=json.loads(response.content)
# print(type(jsonresponse))

# url="http://httpbin.org/get"
# response=requests.get(url)
# print(response.content.decode())
# jsonresponse= json.loads(response.content)
# print(type(jsonresponse))

# for claves , valor in jsonresponse.items():
#     print(claves)
#     if isinstance (valor , dict):
#         for i in valor:
#             print(i)