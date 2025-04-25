from django.shortcuts import render
from PearlM.models import *

# Create your views here.

def Show_PMclub(request):
    product_list = product_PMclub.objects.all()
    return render(request,'PMCLUB_HOME.html',{'product_list':product_list})


