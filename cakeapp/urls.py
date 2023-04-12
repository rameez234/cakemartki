
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('',views.first,name='first'),
    path('first', views.first,name = 'first'),
    path('first', views.first, name='first'),
    path('show', views.show, name='show'),
    path('second', views.second, name='second'),
    path('form', views.form, name='form'),
    path('login', views.login, name='login'),
    path('ltable', views.ltable, name='ltable'),
    path('lform', views.lform, name='lform'),
    path('user', views.user, name='user'),
    path('cform', views.cform, name='cform'),
    path('ctable', views.ctable, name='ctable'),
    path('admin1', views.admin1, name='admin1'),
    path('table', views.table, name='table'),
    path('cdisplay', views.cdisplay, name='cdisplay'),
    path('buy', views.buy, name='buy'),
    path('orderdetails', views.orderdetails, name='orderdetails'),
    path('new', views.new, name='new'),
    path('orders', views.orders, name='orders'),
    path('product',views.product,name='product'),
    path('few', views.few, name='few'),
    path('one', views.one, name='one'),
    path('cab', views.cab, name='cab'),
    path('index', views.index, name='index'),
    path('about', views.about, name='about'),
    path('menu', views.menu, name='menu'),
    path('team', views.team, name='team'),
    path('contact', views.contact, name='contact'),
    path('cart', views.cart, name='cart'),
    path('ulogout', views.ulogout, name='ulogout'),
]
