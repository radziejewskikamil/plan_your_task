# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from .models import Tasks
from .forms import TaskForm


def homepage(request):
    """Return all tasks."""
    return render_to_response('index.html', {'tasks': Tasks.objects.all().order_by('date')})


def add_task(request):
    """
    Adds task to database.
    Redirect to homepage in case of success or
    return to form in case of error.
    """
    try:
        if request.method == 'POST':
            form = TaskForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/')
            else:
                return render(request, 'add_edit.html', {'form': form})

        form = TaskForm()
        return render(request, 'add_edit.html', {'form': form})
    except Exception as e:
        print e


def edit_task(request, task_id):
    """
    Edit task in database.
    Redirect to homepage in case of success or
    return to form in case of error.
    param: task_id
    """
    try:
        task = Tasks.objects.get(id=task_id)
        form = TaskForm(instance=task)

        if request.method == 'POST':
            form = TaskForm(request.POST, instance=task)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/')

        return render(request, 'add_edit.html', {'form': form, 'task_id': task_id})
    except Exception as e:
        print e


def delete_task(request, task_id):
    """
    Delete task from database.
    Redirect to homepage.
    param: task_id
    """
    try:
        task = Tasks.objects.get(id=task_id)
        task.delete()
        return HttpResponseRedirect('/')
    except Exception as e:
        print e
