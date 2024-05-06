from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

def home(request):
    name= "Ashis Singh"
    age= 26
    mobileno=8487840633
    mydata = {'nm': name,'a':age,'mo':mobileno}
    return render(request,'home.html',mydata)