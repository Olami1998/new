from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http  import HttpResponse
from .forms import NewUserForm
from django.contrib import messages

# Create your views here.

def register(request):
    """register a new user."""
    if request.method == 'POST':
        #display blank registration form.
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "registration successful")
            return redirect("home:home")
        messages.error(request, "unsuccessful registration. invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="accounts/register.html", context={"register_form":form})



def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("home:home")
            else:
                messages.error(request,"Invalid username or password.")
        else:
           messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="accounts/login.html", context={"login_form":form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.") 
    return redirect("accounts:logout")