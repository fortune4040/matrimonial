from django.urls import path
from .views import *
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
urlpatterns =[
    path('', auth_views.LoginView.as_view(template_name='homepage.html'),name='home'),
    path('accounts/logout/', auth_views.LogoutView.as_view(),name='logout'),
    path('register',Register.as_view(),name='register'),
    path('detail/',TemplateView.as_view(template_name='agreement.html'),name='agree'),
    path('change_password/',auth_views.PasswordChangeView.as_view(template_name='password_change_form.html',success_url=reverse_lazy('info:password_change_done')),name='change_password'),
    path('change_password_done/',auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),name='password_change_done'),
    path('welcome/',login_required(TemplateView.as_view(template_name='user_profile.html'),login_url='/'),name='welcome'),
    path('profile/',ProfileDetail.as_view(),name='detail'),
    path('profile_update/<int:pk>',ProfileUpdate.as_view(),name='update'),


]
