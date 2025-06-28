from django.db import models

# Create your models here.
class CreateTodo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    isComplete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = 'To Do'

    def __str__(self):
        return self.title
