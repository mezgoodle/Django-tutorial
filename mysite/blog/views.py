from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def index(request):
    tasks = Task.objects.all().order_by('-id')
    return render(request, 'blog/index.html', {'tasks': tasks})

def about(request):
    return render(request, 'blog/about.html')

def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:index')
        else:
            error = 'Form is invalid'
    form = TaskForm()
    context = {
        'form': form,
        'error': error,
    }
    return render(request, 'blog/create.html', context)