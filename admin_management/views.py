from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, redirect, render, reverse

def login_page(request):
    if request.user.is_authenticated:
        return redirect(reverse("student_list"))
    return render(request, 'login.html')
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

from django.contrib.auth import authenticate, login
from django.http import JsonResponse

def login_view(request):
    if request.method == 'POST':
        print('hhh')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)
        print(user,"user")
        if user is not None:
            print("hhh")
            login(request, user)
            return render(request, 'home.html')
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')
