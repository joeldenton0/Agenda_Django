from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
from django.contrib import messages

def index(request):  # Vista para renderizar filtrado por barra de busqueda.
    todos = Todo.objects.filter(title__icontains=request.GET.get('search', ''))

    context = {
        'todos' : todos
    }

    return render(request, 'todo/index.html', context)

def sorted_index(request, order):  # Vista para renderizar lista de tareas en orden ascendente o descendente.
    if order.startswith('-'):
        order_field = order[1:]
        todos = Todo.objects.all().order_by('-' + order_field)
        current_order = '-' + order_field  # Agregar el signo menos al orden actual
    else:
        order_field = order
        todos = Todo.objects.all().order_by(order_field)
        current_order = order

    context = {
        'todos': todos,
        'current_order': current_order
    }

    return render(request, "todo/index.html", context)

def view(request, id):  # Vista para renderizar detalles de tarea.
    todo = Todo.objects.get(id=id)
    context = {
        'todo': todo
    }

    return render(request, "todo/detail.html", context)

def edit(request, id):  # Vista para editar tarea.
    todo = Todo.objects.get(id=id)
    if request.method == 'GET':
        form = TodoForm(instance= todo)
        context = {
            'form' : form,
            'id' : id
        }

        return render(request, "todo/edit.html", context)

    if request.method == 'POST':
        form = TodoForm(request.POST, instance= todo)
        if form.is_valid():
            form.save()
            context = {
                'form' : form,
                'id' : id
            }
            messages.success(request, 'Tarea actualizada.')
            return render(request, "todo/edit.html", context)

def create(request):  # Vista para añadir nueva tarea.
    if request.method == 'GET':
        form = TodoForm()
        context = {
            'form' : form
        }
        return render(request, "todo/create.html", context)

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')

def delete(request, id):  # Vista para borrar tarea.
    del_todo = Todo.objects.get(id=id)
    if request.method == 'POST':
        del_todo.delete()
        return redirect('todo')

    return render(request, 'todo/delete_todo.html', {'id': id})