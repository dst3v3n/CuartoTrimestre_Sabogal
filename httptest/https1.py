import requests

url = "https://eventosgrupo.000webhostapp.com/"
response = requests.get(url)
file = open ("httptest/index.html", "wb")
file.write(response.content)
file.close()


url = "https://eventosgrupo.000webhostapp.com/style.css"
response = requests.get(url)
file = open ("httptest/style.css", "wb")
file.write(response.content)
file.close()

url = "https://eventosgrupo.000webhostapp.com/script.js"
response = requests.get(url)
file = open ("httptest/script.js", "wb")
file.write(response.content)
file.close()

url = "https://eventosgrupo.000webhostapp.com/logo.jpg"
response = requests.get(url)
file = open ("httptest/logo.jpg", "wb")
file.write(response.content)
file.close()

url = "https://eventosgrupo.000webhostapp.com/imagen5.jpg"
response = requests.get(url)
file = open ("httptest/imagen5.jpg", "wb")
file.write(response.content)
file.close()

url = "https://eventosgrupo.000webhostapp.com/imagen1.png"
response = requests.get(url)
file = open ("httptest/imagen1.png", "wb")
file.write(response.content)
file.close()

url = "https://eventosgrupo.000webhostapp.com/imagen2.webp"
response = requests.get(url)
file = open ("httptest/imagen2.webp", "wb")
file.write(response.content)
file.close()

url = "https://eventosgrupo.000webhostapp.com/imagen3.png"
response = requests.get(url)
file = open ("httptest/imagen3.png", "wb")
file.write(response.content)
file.close()

url = "https://eventosgrupo.000webhostapp.com/imagen4.jpg"
response = requests.get(url)
file = open ("httptest/imagen4.jpg", "wb")
file.write(response.content)
file.close()