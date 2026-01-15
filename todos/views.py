from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from .models import Task
from django.core.exceptions import ObjectDoesNotExist

def home(request):
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        Task.objects.create(title=title)
        return redirect('home')
    return redirect('home')

def toggle_task(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
        task.completed = not task.completed
        task.save()
        return redirect('home')
    except ObjectDoesNotExist:
        messages.error(request, 'Task not found!')
        return redirect('home')

def delete_task(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
        task.delete()
        return redirect('home')
    except ObjectDoesNotExist:
        messages.error(request, 'Task not found!')
        return redirect('home')
