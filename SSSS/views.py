from django.shortcuts import render
from SSSS.models import *

# Create your views here.

def Home(request):
    list_of_artist = SSSS_artist.objects.all()
    return render(request,'Home_ss.html',{'artist_name':"benny boro's",'artist_list':list_of_artist})

def Product(request,artist_name):
    list_of_products = SSSS_products.objects.all()
    return render(request,'Collection_products.html',{'list_of_products':list_of_products,'artist_name':artist_name})

