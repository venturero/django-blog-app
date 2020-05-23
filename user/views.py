from django.shortcuts import render,redirect
from . forms import RegisterForm,LoginForm   
from django.contrib import messages#mesajlarda danger yok dikkat!
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout #user ı verirsen user sisteme kayıt olmuş oluyor
#authenticate kullanıcının olup olmadığını sorguluyor
# Create your views here.


def register(request):
    form = RegisterForm(request.POST or None)#get de olsa post ta olsa formu oluşturuyoruz

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        newUser = User(username=username)
        newUser.set_password(password)

        newUser.save()  
        login(request,newUser)
        messages.info(request, 'Başarıyla kayıt oldunuz.')#" kesme işareti değil tırnak işareti kesme de olabilir
        return redirect("index")
    context = {
            "form": form    
        }
    return render(request,"register.html",context)  


def loginUser(request):
    form = LoginForm(request.POST or None)

    context = {
        "form":form
    }

    if form.is_valid():#form clas ın içindeki clean çağırılıyor
        username = form.cleaned_data.get("username")#clean değil cleaned
        password = form.cleaned_data.get("password")

        user = authenticate(username = username,password = password)
        
        if user is None:
            messages.info(request,"Kullanıcı Adı veya Parola hatalı")
            return render(request,"login.html",context)

        messages.success(request,"Başarıyla giriş yaptınız")#success iki(2) s ile
        login(request,user)#kullanıcı giriş yaptı
        return redirect("index")
    return render(request,"login.html",context)
def logoutUser(request):
    logout(request)
    messages.success(request,"Başarıyla Çıkış Yaptınız")
    return redirect("index")
    
