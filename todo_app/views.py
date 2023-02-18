from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Task
from .forms import TaskForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def main_view(request):
    template = 'todo_app/task_list.html'
    context = {}
    context['tasks'] = Task.objects.all().order_by('-complete')
    context['tasks'] = context['tasks'].filter(author=request.user)
    search_input = request.GET.get('search-area') or ''
    if search_input:
        context['tasks'] = context['tasks'].filter(title__startswith=search_input)
    context['search_input'] = search_input
    return render(request, template, context)
        

@login_required
def task_create(request):
    template = 'todo_app/task_create.html'
    context = {}
    form = TaskForm(request.POST or None)
    if form.is_valid():
        form = form.save(commit=False)
        form.author = request.user
        form.save()
        return HttpResponseRedirect(reverse('task_list'))
    context['form'] = form
    return render(request, template, context)

@login_required
def task_detail(request, pk):
    template = 'todo_app/task_detail.html'
    context = {}
    context['data'] = Task.objects.get(pk=pk)
    return render(request, template, context)

@login_required
def task_update(request, pk):
    template = 'todo_app/task_update.html'
    context = {}
    obj = get_object_or_404(Task, pk=pk)
    form = TaskForm(request.POST or None, instance=obj)
    if form.is_valid():
        form = form.save()
        return HttpResponseRedirect(reverse('task_list'))
    context['form'] = form
    return render(request, template, context)

@login_required
def task_delete(request, pk):
    template = 'todo_app/task_delete.html'
    context = {}
    obj = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return HttpResponseRedirect(reverse('task_list'))
    return render(request, template, context)
    