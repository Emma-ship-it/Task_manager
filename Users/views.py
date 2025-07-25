from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def signup(request):
    sign_up_form = UserCreationForm()
    if request.method == "POST":
        sign_up_form = UserCreationForm(request.POST)
        if sign_up_form.is_valid():
            sign_up_form.save()
            messages.success("Account created successfully")
            return redirect('users:login')
    return render(request,'Users/signup.html',{'form':sign_up_form})    
