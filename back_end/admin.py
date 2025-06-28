from django.contrib import admin
from .models import CreateTodo

# Register your models here.

class CreateTodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'isComplete', 'created_at', 'updated_at')
    search_fields = ('title', 'description')
    list_filter = ('isComplete', 'created_at', 'updated_at')

admin.site.register(CreateTodo, CreateTodoAdmin)
