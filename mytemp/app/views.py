from django.shortcuts import render
from django.shortcuts import HttpResponse
from datetime import datetime
# Create your views here.

def home(request):
        students = {'names':['Ashish','Rahul','Rajan','virendra']}
        return render(request,'home.html',students)
    
    
