from django.shortcuts import render,redirect,get_object_or_404
from .models import Tasks,Category,Priority
from .forms import CreateTaskForm 

# Create your views here.
def home(request):
    return render(request,'task/index.html')

def dashboard(request):
    to_do = Tasks.objects.filter(category = Category.TO_DO)
    progress = Tasks.objects.filter(category = Category.Progress)
    complete = Tasks.objects.filter(category = Category.Completed)
    return render(request,'task/dashboard.html',{"TODO":to_do,'progress':progress,'complete': complete})


def task_detail(request, task_id):
    task = get_object_or_404(Tasks,pk=task_id)
    return render(request,'task/task_detail.html',{'task':task})

def add_task(request):
    add_task_form = CreateTaskForm()
    if request.method == 'POST':
        add_task_form = CreateTaskForm(request.POST)  
        if add_task_form.is_valid():
            add_task_form.save()  
            return redirect('task:dashboard')
        else:
            print(add_task_form.errors)
    return render(request,'task/create_task.html',{"form" : add_task_form})    

def edit_task(request,id):
    task=get_object_or_404(Tasks,pk=id)  
    form = CreateTaskForm(instance = task) 
    if request.method == "POST":
        form = CreateTaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('task:detail',task_id=id)
    return render(request,'task/edit_task.html',{"form":form,"task":task})     

def confirm_delete(request,id):
    task = get_object_or_404(Tasks,pk=id)
    return render(request,'task/confirm_delete.html',{"task":task})
def delete_task(request,id):
    task = get_object_or_404(Tasks,pk=id)
    if request.method == "POST":
        task.delete()
        return redirect("task:dashboard")
    
    
    