from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib import messages
from .forms import RegisterForm, ProfileForm
from .models import User, Profile
from rest_framework import generics
from rest_framework import mixins
from .serializers import ProfileSerializers
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import status
from rest_framework.views import APIView


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


class ProfileDetail(APIView):
    serializer_class = ProfileSerializers
    queryset = Profile.objects.all()
    lookup_field = 'id'
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, id=None):
        form = ProfileForm()
        return Response({'form':form},template_name='create_profile.html')


    def post(self, request):
        data = request.data
        serializer = ProfileSerializers(data=data)
        print(data)
        if serializer.is_valid():
            serializer.save()
            return redirect('info:home')
        print(serializer.errors)
        return redirect('info:register')
