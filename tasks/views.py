from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from tasks.models import Task
from tasks.forms import newTask
from django.utils import timezone

def index(request):
    task_list = Task.objects.all().order_by('-due_date')[:10]
    return render_to_response('tasks/index.html', {'task_list': task_list})

def new_task(request):
    if request.method == 'POST':
        form = newTask(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            t = Task(task = cd['task'], due_date = cd['due_date'], complete = False)
            t.save()
            print "Did this fucking work???!!!!"
            return HttpResponseRedirect('/tasks/')
    else:
        form = newTask()
        
    return render_to_response('tasks/new_task.html', {
        'form' : form }, 
        )

