from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django import views
from django.contrib.auth import authenticate, login as dj_login


from .forms import SignupForm


class signupView(views.View):
    def post(self,request):
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('User created successfully!')
        return HttpResponse(f"{form.errors}")


class loginView(views.View):
    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user:
            dj_login(request, user)
            return HttpResponse('Login completed!')
        return HttpResponse('Wrong password/username')

