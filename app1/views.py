from multiprocessing import context
from re import template
from django.shortcuts import redirect, render
from .forms import BookForm
from .models import Book
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class AddBook(LoginRequiredMixin,View):
    template_name = 'app1/addbook.html'
    form = BookForm
    def get(self,request):
        form = self.form()
        context = {'form':form}
        return render(request,self.template_name,context)
    def post(self,request):
        form = self.form(request.POST)
        context = {'form':form}
        if form.is_valid():
            form.save()
            return redirect("showbookurl")
        return render(request,self.template_name,context)

class StudentView(LoginRequiredMixin,View):
    template_name = 'app1/showbook.html'
    def get(self,request):
        obj = Book.objects.all()
        context = {'obj':obj}
        return render(request,self.template_name,context)

class BookUpdate(LoginRequiredMixin,View):
    template_name = 'app1/addbook.html'
    form = BookForm
    def get(self,request,id):
        data = Book.objects.get(id=id)
        form = self.form(instance=data)
        context = {'form':form}
        return render(request,self.template_name,context)
    def post(self,request,id):
        data = Book.objects.get(id=id)
        form = self.form(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect("showbookurl")
        context = {'form':form}
        return render(request,self.template_name,context)        
    
class DeleteBook(LoginRequiredMixin,View):
    def get(self,request,id):
        obj = Book.objects.get(id=id)
        obj.delete()
        return redirect("showbookurl")