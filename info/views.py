from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib import messages
from .forms import RegisterForm
from .models import User
def HomePage(request):
    return render(request,'homepage.html')


class Register(View):
    def get(self,request):
        form = RegisterForm()
        context = {'form':form}
        return render(request,'register.html',context=context)

    def post(self,request):
        data = request.POST
        form = RegisterForm(data)
        if form.is_valid():
            form.save()
            messages.success(request, "SuccessFully registered to Shubh Vivah Sansta !")
            return redirect('info:home')
        messages.error(request, form.errors)
        return redirect('info:register')

class CreateProfile(View):
    def get(self,request):
        return render(request,'create_profile.html')

    def post(self,request):
        data = request.POST
        print(data)
        return render(request,'create_profile.html')

