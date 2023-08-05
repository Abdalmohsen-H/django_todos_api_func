from django.contrib import admin

# Register your models here to be able to manage it from django admin dashboard.
from .models import Tasks

admin.site.register(Tasks)
