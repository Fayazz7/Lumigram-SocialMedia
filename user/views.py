from django.shortcuts import render, redirect
from django.views.generic import View, CreateView, TemplateView
from user.forms import RegistrationForm, LogInForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
# Create your views here.


class UserAuthView(View):
    def get(self, request, *args, **kwargs):
        signup_form = RegistrationForm()
        signin_form = LogInForm()
        return render(request, "signup.html", {"signup_form": signup_form, "signin_form": signin_form})

    def post(self, request, *args, **kwargs):
        signup_form = RegistrationForm(request.POST)
        signin_form = LogInForm(request.POST)

        if 'signup' in request.POST:
            if signup_form.is_valid():
                print(signup_form.cleaned_data)
                signup_form.save()
                return render (request,"signup.html")
            else:
                return render (request,"signup.html",{"signup_form":signup_form})
        elif 'signin' in request.POST:
            if signin_form.is_valid():
                print(signin_form.cleaned_data)
                user=authenticate(request,username=signin_form.cleaned_data.get("username"),password=signin_form.cleaned_data.get("password"))
                if user:
                    login(request,user)
                    print("success")
                    return redirect ('home')
                else:
                    print("Failed")
            else:
                return render (request,"signup.html",{"signin_form":signin_form})
            
class SignOutView(View):
    def get (self,request,*args, **kwargs):
        logout(request)
        return redirect ('authentication')


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "index.html")
