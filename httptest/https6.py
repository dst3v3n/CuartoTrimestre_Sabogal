import requests
url = "https://cdn.computerhoy.com/sites/navi.axelspringer.es/public/media/image/2023/04/raspberry-lanza-editor-codigo-aprender-python-lenguaje-ia-3008158.jpg?tf=3840x"
response = requests.get (url , stream=True)

with open ("httptest/donwnload.jpg" , "wb") as image:
    for pedazo in response.iter_content():
        image.write(pedazo)