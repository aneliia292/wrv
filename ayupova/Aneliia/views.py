from django.shortcuts import render
from django.http import HttpResponse

def index(request, age, hobby):
    return HttpResponse(f'<h4>I am {age}. <br>My hobby is {hobby}')

def about(request, sity, study):
    return HttpResponse(f'<h4>About me: <h4>I am from {sity}. <br>My Studing is {study}. ')

def contscts(request, number):
    return HttpResponse(f'<h1>My number: {number}')

def NotFound(request):
    return HttpResponse('NotFound')