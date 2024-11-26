from django.db import models


from django.db import models
from django.contrib.auth.models import User  # For assigning tasks to specific users

class TodoItem(models.Model):
    title = models.CharField(max_length=200, help_text="Title of the task")
    description = models.TextField(blank=True, null=True, help_text="Detailed description of the task")
    created_at = models.DateTimeField(auto_now_add=True, help_text="When the task was created")
    updated_at = models.DateTimeField(auto_now=True, help_text="When the task was last updated")
    due_date = models.DateTimeField(blank=True, null=True, help_text="Optional due date for the task")
    is_completed = models.BooleanField(default=False, help_text="Mark task as completed")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todos', help_text="The user this task belongs to")

    class Meta:
        ordering = ['is_completed', 'due_date']  # Prioritize incomplete tasks and sort by due date
        verbose_name = "To-Do Item"
        verbose_name_plural = "To-Do Items"

    def __str__(self):
        return self.title


