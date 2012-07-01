from tasks.models import Task
from django.contrib import admin

class PollAdmin(admin.ModelAdmin):
    list_display = ('task', 'due_date','is_due_soon','complete')
    list_filter = ['due_date',]
    search_fields = ['question']
    date_hierarcy = 'due_date'

admin.site.register(Task, PollAdmin)