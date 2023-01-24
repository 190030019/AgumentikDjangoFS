from email import message
from multiprocessing import context
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages

from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from .decoraters import *
from django.contrib.auth.models import Group
from django.conf import settings  
from django.core.mail import send_mail 
from django.contrib.auth.models import User
def registerUser(request):
    form = CreateUserForm()
    custform=CustomerForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        custform=CustomerForm(request.POST)
        if form.is_valid() and custform.is_valid():
            user=form.save()
            customer=custform.save(commit=False)
            customer.user=user
            customer.email=form.cleaned_data['email']
            customer.save()
            messages.success(request,'account created successfully')
            return redirect('login')
    context={'form':form}
    return render(request,'home1/register.html',context)
@unautheticated_user
def loginpage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,"Username or Password is incorrect")

    return render(request,'home1/login.html')






def management(request):
    Customer=Rcustomer.objects.all()
    coninf=contact_us.objects.all()
    Property=submit_order.objects.filter(delete_status=False)
    Deleted_Properties=submit_order.objects.filter(delete_status=True)
    context={'Customer':Customer,'Property':Property, 'Deleted_Properties': Deleted_Properties,'coninf':coninf}
    return render(request,'home1/management.html',context)


def delcustomer(request,id):
    member=Rcustomer.objects.get(id=id)
    member.delete()
    context={'member':member}
    return render(request,'home1/delcustomer.html')

def imghead1(request):
    img=imghead.objects.all()
    print(img)
    context={'img':img}
    return render(request,'home1/home1.html',context)
@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('home')

def customer(request, pk):
    customer=Rcustomer.objects.get(id=pk)
    Customer1=Rcustomer.objects.all()
    property = submit_order.objects.filter(name=request.user.username)
    context={'customer':customer,'property':property,'Customer1':Customer1}
    return render(request,'home1/customer.html',context)



    


