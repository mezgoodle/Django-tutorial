from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'task', 'status','created_on')
    list_filter = ('id',)
    search_fields = ['title', 'task']

admin.site.register(Task)
