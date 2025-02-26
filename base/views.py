from django.shortcuts import render
from django.http import request, response, HttpResponse, HttpRequest 

# Create your views here.

def tasklist(request):
    return HttpResponse('<h1>To Do List</h1>')