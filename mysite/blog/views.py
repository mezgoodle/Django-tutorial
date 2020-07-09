from django.shortcuts import render
from .models import Task
from .forms import TaskForm

def index(request):
    tasks = Task.objects.all().order_by('-id')
    return render(request, 'blog/index.html', {'tasks': tasks})

def about(request):
    return render(request, 'blog/about.html')

def create(request):
    form = TaskForm()
    context = {
        'form': form
    }
    return render(request, 'blog/create.html', context)