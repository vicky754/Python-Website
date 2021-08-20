from django.shortcuts import render,redirect,HttpResponse
from .forms import UserForm
from django.contrib.auth import authenticate,login,logout
from . models import Category,Product

categoryList=Category.objects.all()
productList=Product.objects.all()
def home(request):
    d={"cl":categoryList,'pl':productList}
    return render(request,"home.html",d)


def addUser(request):
   
    if request.method=='POST':
        u=UserForm(request.POST)
        u.save()
        return redirect("/")
    else:
        u=UserForm
        d={"cl":categoryList,'form':u}
        return render(request,'myform.html',d)

    
def mylogin(request):
    d={"cl":categoryList}

    if request.method=='POST':
        uname=request.POST.get("uname")
        passw=request.POST.get("passw")
        usr=authenticate(request,username=uname,password=passw)
        if usr is not None:
            login(request,usr)
            return redirect("/")
        else:
            return HttpResponse("<h1>Invalid UserName and Passwor</h1>")
    else:
        return render(request,'login.html',d)
    
def logOUT(request):
    logout(request)
    return redirect("/")


def getByCategory(request):
    cid=request.GET.get("cid")
    pl=Product.objects.filter( category_id=cid)
    d={"cl":categoryList,'pl':pl}
    return render(request,'home.html',d)