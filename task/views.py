from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Tasks,Category,Priority
from .forms import CreateTaskForm 

# Create your views here.
def home(request):
    return render(request,'task/index.html')

@login_required
def dashboard(request):
    user= request.user
    tasks = Tasks.objects.filter(added_by = user)
    to_do = tasks.filter(category = Category.TO_DO)
    progress = tasks.filter(category = Category.Progress)
    complete = tasks.filter(category = Category.Completed)
    return render(request,'task/dashboard.html',{"TODO":to_do,'progress':progress,'complete': complete})


def task_detail(request, task_id):
    task = get_object_or_404(Tasks,pk=task_id)
    return render(request,'task/task_detail.html',{'task':task})

def add_task(request):
    add_task_form = CreateTaskForm()
    if request.method == 'POST':
        add_task_form = CreateTaskForm(request.POST)  
        if add_task_form.is_valid():
            new_task = add_task_form.save(commit=False)  
            new_task.added_by = request.user
            new_task.save()
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
    
    
    