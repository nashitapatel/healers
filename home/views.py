from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'index.html')
 #   return HttpResponse("this is home page")

def signup(request):
    if request.method == "POST":
        # username = request.POST.get('username')
        username = request.POST['username']
        email = request.POST['useremail']
        password = request.POST['confirmpassword']
        myuser = User.objects.create_user(username, email, password)

        myuser.save()

        messages.success(request, "Your Account has been Successfully created.")
        return redirect('/login')
        if User.objects.filter(username = username).first():
            messages.error(request, "This username already exist")
            return redirect('login')
        
        else:
           messages.error(request,"User already exists") # your error message
           return redirect(request.path)


    return render(request, 'signup.html')

def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        
        #check if user has entered correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
           # A backend authenticated the credentials
           login(request, user)
           return redirect("/")

        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')

    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")

def foryou(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'foryou.html')

   # return HttpResponse("this is for you page")

def starcorner(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'starcorner.html')

   # return HttpResponse("this is star corner page")

def activities(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'activities.html')

   # return HttpResponse("this is activities page")

def learning(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'learning.html')

   # return HttpResponse("this is learning page") 