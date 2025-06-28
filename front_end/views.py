from django.shortcuts import render
from back_end.models import CreateTodo

# Create your views here.
def index(request):
    all_todos= CreateTodo.objects.all()
    context = {
        'all_todos': all_todos
    }
    return render(request, 'index.html', context)