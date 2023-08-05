from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=150)
    # Auto_now_add adds time on creation action
    created_at = models.DateTimeField(auto_now_add=True)
    # While auto_now adds time on save action
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
