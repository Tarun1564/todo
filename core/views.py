from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def index(request):
    tasks=Task.objects.all().filter(is_completed=False)
    c_tasks=Task.objects.all().filter(is_completed=True)
    return render(request,'index.html',{'tasks':tasks,'c_tasks':c_tasks})
def add_task(request):
    if(request.method=='POST'):
        desc=request.POST['description']
        Task(description=desc).save()
        return redirect('index')
    return redirect('index')
def delete_task(request,id):
    Task.objects.filter(id=id).delete()
    return redirect('index')
def complete_task(request,id):
    Task.objects.all().filter(id=id).update(is_completed=True)
    return redirect('index')