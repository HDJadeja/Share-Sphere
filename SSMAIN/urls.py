from django.urls import path 
from SSMAIN.views import *

urlpatterns = [
     path('',Home,name='SSH'),
     path('logout',logout,name='logging_out'),
     path('admin-login',adminlog_in,name="ss_admin"),
     path('add_in_cart/<int:product_id>/<str:club>',add_in_cart,name="cart_add"),
     path('show_in_cart',show_cart,name="show_cart"),
     path('remove_cart/',remove_from_cart,name="remove_cart"),
]
