from django.shortcuts import render, redirect
from back_end.models import CreateTodo
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    all_todos= CreateTodo.objects.all()
    context = {
        'all_todos': all_todos
    }
    return render(request, 'index.html', context)

def statusComplete(request, pk):
    is_Complete = CreateTodo.objects.get(pk=pk)
    is_Complete.isComplete = not is_Complete.isComplete
    is_Complete.save()
    return redirect('home')

def deleteTodo(request, pk):
    if request.method != 'POST':
        todo = get_object_or_404(CreateTodo, pk=pk)
        todo.delete()
    return redirect('home')