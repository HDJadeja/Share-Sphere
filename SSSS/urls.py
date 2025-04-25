from django.urls import path 
from SSSS.views import *

urlpatterns = [
    path('', Home, name='SSSSHome'),
    path('products/<str:artist_name>',Product,name='ssproduct'),

]
