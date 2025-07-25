from django.shortcuts import render,redirect

# Create your views here.
def home(request):
    return render(request,'task/index.html')

def dashboard(request):
    return render(request,'task/dashboard.html')
    
