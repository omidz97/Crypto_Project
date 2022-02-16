from http.client import HTTPResponse
from pickle import GET
from urllib import request
from django.shortcuts import render,redirect
import csv 
import codecs
from crypto.models import cryptotable,predicttable

def index(request):

    return render(request,'crypto\index.html',{
      
    })

def CryptoView(request):
    
    query_results = cryptotable.objects.all()

    return render(request,'crypto/table.html',{
      'query_results' : query_results
    })

def PredictView(request):
    
    query_predict_results = predicttable.objects.all()

    return render(request,'crypto/predict.html',{
      'query_predict_results' : query_predict_results
    })