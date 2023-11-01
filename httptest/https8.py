import requests

url = 'https://api.github.com/users'
token = "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"
email = "hablack10@gmail.com"
sesion = requests.Session()
sesion.auth = (email , token)
responses = sesion.get(url)

if responses.status_code == 200:
    responses1 = sesion.get("https://github.com/dst3v3n")
    print(responses1.cookies)
    # print(responses1.content)