# import requests
# import json

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

import requests
import json
url="http://httpbin.org/get"
response=requests.get(url)
print(response.content.decode())
print(type(response.content.decode()))
jsonresponse=json.loads(response.content)
print(type(jsonresponse))


for i in jsonresponse:
    print(i)
    