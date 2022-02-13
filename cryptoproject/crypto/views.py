from http.client import HTTPResponse
from pickle import GET
from urllib import request
from django.shortcuts import render,redirect



def index(request):
    text = [
        {'title':'omid'},
    ]
    return render(request,'crypto\index.html',{
      
    })

