from django.db import models
from django.utils import timezone
import datetime

class Task(models.Model):
    task = models.CharField(max_length=300)
    due_date = models.DateTimeField()
    complete = models.BooleanField()
    
    def __unicode__(self):
        return self.task
    
    def is_due_soon(self):
        return self.due_date <= timezone.now() + datetime.timedelta(days = 1) 
    is_due_soon.admin_order_field = 'due_date'
    is_due_soon.boolean = True
    is_due_soon.short_description = 'Due within 24 hrs?'