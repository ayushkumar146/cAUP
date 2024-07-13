from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
# Create your views here.


def makeup(request):
     print(request.method)
     if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.info(request,'User with this username does not exist')
            return redirect('/auth/mylogin/')
        
        user = authenticate(username=username, password=password)

        if user is None:
            messages.info(request,'invalid password')
            return redirect('/auth/mylogin')
        

        login(request,user)
        messages.info(request,'login successful')

        return redirect(reverse('dashboard:user-homepage', args=[user.id]))
    
     template = loader.get_template('mylogin.html')
     context ={}
     return HttpResponse(template.render(context,request))

def makedown(request):
    print(request.method)
    if (request.method == 'POST'):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        print(password,password2)
        if (password != password2):
            messages.error(request, 'Passwords do not match')
            return redirect('/auth/myregister/')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'User with this username already exists')
            return redirect('/auth/myregister/')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'User with this email already exists')
            return redirect('/auth/myregister/')
        print("con")
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        messages.success(request, 'User created successfully')
        return redirect('/auth/mylogin/')

    return render(request, 'myregister.html')

def register_user(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username)

        if user.exists():
            messages.info(request,'User with this username already exists')
            return redirect("/auth/register/")
        
        user = User.objects.create_user(username=username)

        user.set_password(password)

        user.save()
        
        messages.info(request,'User created successfully')
        return redirect('/home/Dashboard')
    
    template = loader.get_template('register.html')
    context = {}
    return HttpResponse(template.render(context,request))
    
    

def login_user(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.info(request,'User with this username does not exist')
            return redirect('/auth/login/')
        
        user = authenticate(username=username, password=password)

        if user is None:
            messages.info(request,'invalid password')
            return redirect('/auth/login')
        

        login(request,user)
        messages.info(request,'login successful')

        return redirect('/home/polls/')
    
    template = loader.get_template('login.html')
    context ={}
    return HttpResponse(template.render(context,request))

def logout_user(request):
    logout(request)
    messages.info(request,'logout successful')
    return redirect('/auth/login/')


