from django.shortcuts import render, redirect

from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django import views
from django.contrib.auth import authenticate, login as dj_login, logout as dj_logout

from .forms import SignupForm


class signupView(views.View):
    def post(self, request):
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse('User created successfully!')

        return HttpResponse(f"{form.errors}")


class loginView(views.View):
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user:
            dj_login(request, user)
            return HttpResponse('Login completed!')
        return HttpResponse('Wrong password/username')


class logoutView(views.View):
    @csrf_exempt
    def post(self, request):
        if not request.user.is_authenticated:
            return HttpResponse('Please login first')
        dj_logout(request)
        return HttpResponse('Logout successfully')



class changePassView(views.View):
    def post(self,request):
        if not request.user.is_authenticated:
            return HttpResponse('Please login first')

        old_password = request.POST['old_password']
        new_password1 = request.POST['new_password1']
        new_password2 = request.POST['new_password2']

        if not request.user.check_password(old_password):
            return HttpResponse('Wrong old password')

        if new_password1 != new_password2:
            return HttpResponse('Entered passwords are not identical')

        request.user.set_password(new_password1)
        request.user.save()

        return HttpResponse('Password changed successfully!')
