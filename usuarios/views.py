from django.shortcuts import render
from django.http import HttpResponse

# Em baixo está minhas funções/views

def index(request):
    return HttpResponse("Olá Mundo !")


