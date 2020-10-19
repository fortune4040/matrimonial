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
from django.http.request import QueryDict, MultiValueDict
from django.contrib.auth.mixins import LoginRequiredMixin


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


class ProfileDetail(LoginRequiredMixin,APIView):
    serializer_class = ProfileSerializers
    queryset = Profile.objects.all()
    lookup_field = 'id'
    renderer_classes = [TemplateHTMLRenderer]


    def get(self, request, id=None):
        # print(serializer)
        form = ProfileForm()
        return Response({'user': self.request.user},template_name='create_profile.html')


    def post(self, request):
        new_data ={}
        data = dict(request.data)
        new_data.update(request.POST.dict())
        images = list(map(lambda x: {'image':x}, data.get('images')))
        new_data['images'] = images
        print(new_data)
        serializer = ProfileSerializers(data=new_data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return redirect('info:home')
        print(serializer.errors)
        return redirect('info:register')


from django.views.generic.edit import UpdateView
from .models import Profile


class ProfileUpdate(UpdateView):
    model = Profile
    fields = '__all__'
    template_name_suffix = '_update_form'