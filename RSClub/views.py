from django.shortcuts import render
from RSClub.models import *

# Create your views here.

def RShome(request):
    products = product_RSclub.objects.all()
    return render(request,'RSHOME.html',{'products':products})
