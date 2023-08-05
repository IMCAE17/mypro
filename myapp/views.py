import datetime

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('this is my first Django project')

def home(request):
    return HttpResponse('this is students list')

def date1(request):
    d=datetime.datetime.now()
    return HttpResponse(d)

def index1(request):

    a=[
        {'name':'irsahd','age':18,'email':'i@gmail.com'},
        {'name':'faran','age':19,'email':'f@gmail.com'},
        {'name':'samir','age':12,'email':'s@gmail.com'},
        {'name':'lukman','age':21,'email':'l@gmail.com'},
        {'name':'azim','age':13,'email':'a@gmail.com'},

    ]
    return render(request,'index.html',{'a1':a})

def veg(request):
    b=[
        {'name':'Onion','Price':100,'Quantity':3},
        {'name': 'Tomato', 'Price': 120, 'Quantity': 7},
        {'name': 'Garlic', 'Price': 90, 'Quantity':0},
        {'name': 'Patato', 'Price': 170, 'Quantity': 6}
    ]
    return render(request,'veg.html',{'b1':b})