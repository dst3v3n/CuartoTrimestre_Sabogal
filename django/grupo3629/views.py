from django.http import HttpResponse
from django.shortcuts import render

# def home (request):
#     return HttpResponse('<h1>Hello world Django')

def home (request):
    return render(request , 'home.html')