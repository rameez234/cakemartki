from django.shortcuts import render,redirect

from .models import *
from datetime import date
def first(request):
    # data1=Enter.objects.get()
    # if data1.type == 1:
    #     request.session['username'] = data1.username
    #     return redirect(index)
    #
    # elif data1.type == 0:
    #     request.session['username'] = data1.username
    #     return redirect(admin1)
    return render(request, 'lform.html')
def show(request):
    name = request.POST['name']
    email = request.POST['email']
    phone = int(request.POST['phone'])
    username = request.POST['username']
    password = request.POST['password']
    data1 = Start(name=name, email=email, phone=phone, username=username)
    data1.save()
    data2 = Enter(username=username, password=password, type=1)
    data2.save()
    return render(request, 'lform.html')
def form(request):
    return render(request,'form.html')
def login(request):
    return render(request,'login.html')
def lform(request):
    return render(request, 'lform.html')

def few(request):
    data2 = Enter.objects.all()
    return render(request, 'ltable.html',{'result2':data2})


def second(request):
    data1=Start.objects.all()
    return render(request, 'login.html',{'result1':data1})
def ltable(request):
    return render(request, "ltable.html")
def table(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        data1=Enter.objects.get(username=username, password=password)

        if data1.type == 1:
            request.session['username'] = data1.username
            return redirect(index)

        elif data1.type == 0:
            request.session['username'] = data1.username
            return redirect(admin1)
    return render(request,'lform.html')
def index(request):
    if 'username' in request.session:
        return render(request, "index.html")
    return redirect("/")
def admin1(request):
    if 'username' in request.session:
        return render(request, 'admin1.html')
    return redirect("/")
def ulogout(request):
    if 'username' in request.session:
        request.session.flush()
    return redirect(table)
def product(request):
    cakename=request.POST['cakename']
    cakeid = int(request.POST['cakeid'])
    photo=(request.FILES['photo'])
    description = request.POST['description']
    price= int(request.POST['price'])
    data3=Item(cakename=cakename,cakeid=cakeid,photo=photo,description=description,price=price)
    data3.save()
    return render(request, 'success.html')
def user(request):
    return render(request, 'user.html')
def cform(request):
    return render(request, 'cform.html')
def ctable(request):
    return render(request, 'ctable.html')

def cdisplay(request):
   data3=Item.objects.all()
   return render(request, 'ctable.html',{'result3':data3})


def buy(request):
    username = request.session['username']


    cakename = request.POST['cakename']
    today = date.today()
    fb = Start.objects.get(username=username)
    fbpro = Item.objects.get(id=cakename)
    data4 = Buy(username=fb, cakename=fbpro, date=today)
    data4.save()
    data3 = Item.objects.all()
    return render(request, 'user.html', {'result3': data3, 'msg': "CAKE ordered"})


def orderdetails(request):
    data4 = Buy.objects.all()
    return render(request, 'orders.html', {'result4': data4})


def new(request):
    name = request.session['username']
    data1 =Start.objects.get(username=name)
    return render(request, 'new.html', {'result1': data1})


def orders(request):
    name = request.session['username']
    fb = Start.objects.get(username=name)
    data4 = Buy.objects.filter(username=fb)
    return render(request, 'orders.html', {'result4': data4})
def one(request):
    return render(request, "first.html")

def cab(request):
    data3 = Item.objects.all()
    return render(request, 'user.html', {'result3': data3})


def about(request):
    return render(request, "about.html")
def menu(request):
    return render(request, "menu.html")
def team(request):
    return render(request, "team.html")
def contact(request):
    return render(request, "contact.html")
def cart(request):
    data3 = Item.objects.all()
    return render(request, "cart.html", {'result3': data3})









