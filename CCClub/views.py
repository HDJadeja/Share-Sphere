from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from CCClub.models import *
# Create your views here.

def Home(request):
    template = loader.get_template('CC_home.html')
    return HttpResponse(template.render({'products':product_CCClub.objects.all()},request))


