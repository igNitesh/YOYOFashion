from .components.auth import *
from .components.cart import cart
from .components.order import order
from .components.your_order import Your_orderView
from .components.index import index
from .components.shop_details import shop_details
from .components.shop import *
from .components.address import Address ,edit_address
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('',index.as_view() , name='homepage'),
    path('shop', shop.as_view() , name='shop'),
    path('shop/<slug:filter_slug>/', shop.as_view(), name='shop'),
 
    path('signup',signup.as_view(),name='signup'),
    path('address', Address.as_view(), name='address'),
    path('login',login.as_view(),name='login'),
    path('your_order',Your_orderView.as_view(),name='your order'),
    path('logout',logout,name='logout'),
    path('edit-address',edit_address,name='edit_address'),
    path('cart',cart.as_view(),name='cart'),
    path('order',order.as_view(),name='order'),
    path('shop_details',shop_details.as_view(),name='shop_details'),
    # path('serach',search_view,name='seacrh_view')
]
