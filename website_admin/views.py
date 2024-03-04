from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

from website_admin.models import User




# Create your views here.
def admin_login(request):
    if request.method == "POST":
        username = request.POST["name"]
        password = request.POST["password"]

        print(username)
        print(password)

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login Sucessfull')
            return redirect('home')
        else:
            messages.error(request, 'Login Failed. Please check your credentials')
            
    return render(request,"admin.html")

def admin_register(request):
    if request.method == "POST":
        firstname = request.POST["first-name"]
        lastname = request.POST["last-name"]
        email = request.POST["email"]
        new_username = request.POST["username"]
        new_password = request.POST["password"]
        confirm_password = request.POST["confirm-password"]
        if(new_password != confirm_password):
            messages.error(request, "Confirm password not equal to new password")
            return redirect('admin_register')
        
        if User.objects.filter(email=email, username= new_username).exists():
            messages.info(request, 'Email or username already exist')
            return redirect('admin_register')
    
        register_user = User.objects.create(first_name=firstname, last_name=lastname, email=email, username=new_username)
        register_user.set_password(new_password)
        register_user.save()

        if register_user:
            messages.success(request, 'Registered sucessfully, Please Login')
            return redirect('admin_login')

    return render(request,"register.html")

def logout(request):
    return render(request, "admin.html")


