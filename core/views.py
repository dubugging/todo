from django.shortcuts import render, redirect
from .models import Task


def home(request):
    tasks = Task.objects.all()
    return render(request, template_name='core/home.html', context={'tasks': tasks})


def add_task(request):
    new_task = request.POST['new_task']
    Task.objects.create(task=new_task)
    return redirect('home')


def delete_task(request, pk):
    Task.objects.filter(pk=pk).delete()
    return redirect('home')


def edit_task(request, pk):
    task = Task.objects.get(pk=pk)
    if request.method == 'POST':
        updated_task = request.POST['updated_task']
        task.task = updated_task
        task.save()
        return redirect('home')
    return render(request, template_name='core/edit.html', context={'task': task})
