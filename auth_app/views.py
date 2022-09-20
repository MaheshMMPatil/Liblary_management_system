from multiprocessing import context
from re import template
from django import views
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views import View
from django.contrib.auth import authenticate, login,logout
# Create your views here.

class RegisterView(View):
    form = UserCreationForm
    template_name = 'auth_app/register.html'
    def get(self,request):
        form = self.form()
        context = {'form':form}
        return render(request,self.template_name,context)
    def post(self,request):
        form = self.form(request.POST)
        context = {'form':form}
        if form.is_valid():
            form.save()
        return render(request,self.template_name,context)

class LoginView(View):
    template_name = 'auth_app/login.html'
    def get(self,request):
        context = {}
        return render(request,self.template_name,context)
    def post(self,request):
        context = {}
        u = request.POST.get("un")
        p = request.POST.get("ps")
        user = authenticate(username = u,password=p)
        if user is not None:
            login(request,user)
            return redirect("showbookurl")
        return render(request,self.template_name,context)

class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect("loginurl")


                