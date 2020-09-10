from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .models import Todo
from .forms import TodoForm

def index(request):
    todo_list = Todo.objects.order_by('id')
    todo_exist = Todo.objects.exists()
    form = TodoForm()
    context = {'todo_list': todo_list, 'todo_exist': todo_exist, 'form': form}
    return render(request, 'todo/index.html', context)

@require_POST
def addToDo(request):
    form = TodoForm(request.POST)
    if form.is_valid():
        new_todo = Todo(text = request.POST['text'])
        new_todo.save()
    return redirect('index')

def completeToDo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()
    return redirect('index')

def undoToDo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = False
    todo.save()
    return redirect('index')

def deleteCompleted(request):
    Todo.objects.filter(complete__exact=True).delete()
    return redirect('index')

def deleteAdd(request):
    Todo.objects.all().delete()
    return redirect('index')