from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.models import User

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()      # враќа User
            login(request, user)
            return redirect("index")
    else:
        form = UserCreationForm()
    return render(request, "appp/register.html", {"form": form})

def index(request):
    error = None
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not username or not password:
            error = "Пополнете ги сите полиња."
        elif User.objects.filter(username=username).exists():
            error = "Корисничкото име веќе постои."
        else:
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            return redirect('index')
    return render(request, "appp/index.html", {"error": error} if error else {})