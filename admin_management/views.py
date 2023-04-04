from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, redirect, render, reverse

from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.contrib.auth.backends import ModelBackend


def login_page(request):
    if request.user.is_authenticated:
        return redirect(reverse("student_list"))
    return render(request, 'login.html')

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None

def login_view(request):
    if request.method == 'POST':

        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse("student_list"))
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')
