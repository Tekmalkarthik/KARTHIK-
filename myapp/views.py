from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from myapp import models
from django.http import response

def home(request):
    return render(request,'Home.html')

def userdata(request):
    response=render(request,'userdata.html')
    return response

def formlink1(request):
     return render(request,"formlink1.html")  

def insertdata(request):
     return render(request,'insertdata.html')     


def Form_2(request):
    rec=models.person.objects.all()         
    d={'data':rec,
       'title':'person_data'}
    return render(request,'Form_2.html',d) 

def Form_3(request):
     return render(request,'Form_3.html')

def Form_4(request):
     return render(request,'Form_4.html')

def Form_5(request):
     return render(request,'Form_5.html')

def Form_6(request):
     return render(request,'Form_6.html')

def Form_7(request):
     return render(request,'form_7.html')

def Form_8(request):
     return render(request,'form_8.html')

def Form_9(request):
     return render(request,'form_9.html')

def Form_10(request):
     return render(request,'form_10.html')

def Form_11(request):
     return render(request,'form_11.html')                             

def Form_12(request):
     return render(request,'form_12.html')  

def kar(request):
     return render(request,'kar.html')  



@login_required(login_url='login')
def save_data(request):
    if request.method == 'POST':
        s1=models.person()
        s1.FristName=request.POST['FirstName']
        s1.LastName=request.POST['LastName']
        s1.Email=request.POST['Email']
        s1.Contact=request.POST['Contact']
        s1.Gender=request.POST['Gender']
        s1.DOB=request.POST['DOB']
        s1.City=request.POST['city']
        s1.address=request.POST['address']
        s1.password=request.POST['password']
        s1.repassword=request.POST['repassword']
        print( s1.FristName, s1.LastName,s1.Email,s1.Contact,s1.Gender,s1.DOB,
        s1.City, s1.address, s1.password,s1.repassword,s1.uploadphoto)
        s1.save()   



def mylogin(request):
    return render(request,'login.html')


def signin(request):
    if request.method == 'POST':
       username= request.POST['username']
       password= request.POST['password']
       print(username)
       print(password)
       user = authenticate(request,username=username,password=password)
       print(user)
       if user:
          login(request,user)    
       else:
           return HttpResponse('invalid credentials')
    return redirect(home)
        

def formlink(request):
    return render(request,"formlink.html")    

  

