from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render,redirect

from django.http import HttpResponse

# Create your views here.
def logout(request):
    auth.logout(request)
    return redirect('/')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass1']
        user = auth.authenticate(usernamr=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid request")
            return redirect('login')

    return render(request, "login.html")


def register(request):
    if request.method=='POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['pass1']
        cpassword = request.POST['pass2']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"user name already exists")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email already exists")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)
                user.save();
                return redirect('login')
        else:
            messages.info(request,'password not matched')
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")