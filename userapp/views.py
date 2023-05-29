from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import User
from django.views.generic import View


# Create your views here.

def home(request):
    return render(request, "index.html")


class UserRegistration(View):

    def post(self, request):
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        phone = request.POST['phone']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username=username, first_name=fname, last_name=lname, phone=phone,
                                          email=email, password=pass1)
        # myuser.save()
        messages.success(request,
                         "Your Account has been created succesfully!!"
                         " Please check your email to confirm your email address "
                         "in order to activate your account.")
        return redirect('signin')

    def get(self, request):
        return render(request, "register.html")


class UserLogin(View):
    def post(self, request):
        if request.method == 'POST':
            username = request.POST['username']
            pass1 = request.POST['pass1']

            user = authenticate(username=username, password=pass1)

            if user is not None:
                login(request, user)
                fname = user.first_name
                # messages.success(request, "Logged In Sucessfully!!")
                return render(request, "index.html", {"fname": fname})
            else:
                messages.error(request, "Bad Credentials!!")
                return redirect('home')

    def get(self, request):
        return render(request, "login.html")


def logout_user(request):
    if request.method == 'GET':
        logout(request)
        messages.success(request, "Logged Out Successfully!!")
        return redirect('home')
