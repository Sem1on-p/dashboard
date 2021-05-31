from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from . import models

# Create your views here.
def void(request):
    return redirect('dashboard')

def dashboard(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            event_list = models.Event.objects.all().order_by('-id')
        elif request.method=='POST':
            event_list = models.Event.objects.all().order_by('-id')
            for i in request.POST:
                print(f'{i}: {request.POST[i]}')
        all_page_status = True
        return render(request, 'index.html', {'event_list': event_list, 'all_page_status':all_page_status})
    else:
        return redirect('myLogin')

def potential(request):
    if request.user.is_authenticated:
        event_list = models.Event.objects.filter(event_status='potential').order_by('-id')
        potential_page_status = True
        return render(request, 'index.html', {'event_list': event_list, 'potential_page_status': potential_page_status})
    else:
        return redirect('myLogin')

def job(request):
    if request.user.is_authenticated:
        event_list = models.Event.objects.filter(event_status='job').order_by('-id')
        job_page_status = True
        return render(request, 'index.html', {'event_list': event_list, 'job_page_status': job_page_status})
    else:
        return redirect('myLogin')

def end_event(request):
    if request.user.is_authenticated:
        event_list = models.Event.objects.filter(event_status='completed').order_by('-id')
        end_event_page_status = True
        return render(request, 'index.html', {'event_list': event_list, 'end_event_page_status': end_event_page_status})
    else:
        return redirect('myLogin')

def view_event(request, event_id):
    if request.user.is_authenticated:
        event = models.Event.objects.get(id=event_id)
        return render(request, 'view_event.html',{'event':event})
    else:
        return redirect('myLogin')

def tasks(request):
    active_tasks = True
    if request.user.is_authenticated:
        if request.method == 'GET':
            task_list = models.Task.objects.all()
            personal = models.Personal.objects.all()
        elif request.method == 'POST':
            a = models.Task()
            a.text = request.POST['text']
            a.executor = models.Personal.objects.get(id= int(request.POST['personal']))
            a.date = request.POST['date']
            a.save()
            task_list = models.Task.objects.all()
            personal = models.Personal.objects.all()
        return render(request, 'task.html', {'task_list':task_list, 'personal':personal, 'active_tasks':active_tasks})
    else:
        return redirect('myLogin')

def delete_task(request, task_id):
    b =models.Task_archive()
    b.text = models.Task.objects.get(id=task_id).text
    b.date = models.Task.objects.get(id=task_id).date
    b.executor = models.Task.objects.get(id=task_id).executor
    b.save()
    models.Task.objects.get(id=task_id).delete()
    return redirect('tasks')

def tasks_archive(request):
    archive_tasks = True
    if request.user.is_authenticated:
        if request.method == 'GET':
            task_list = models.Task_archive.objects.all()
            personal = models.Personal.objects.all()
        return render(request, 'task.html',
                      {'task_list': task_list, 'personal': personal, 'archive_tasks': archive_tasks})
    else:
        return redirect('myLogin')