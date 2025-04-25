from django.urls import path
from PearlM.views import *

urlpatterns = [
    path('',Show_PMclub,name='pmclub')
]