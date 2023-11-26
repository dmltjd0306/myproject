# myapp/views.py
from django.shortcuts import render

def homepage(request):
    return render(request, 'Homepage.html')

def todolist(request):
    return render(request, 'Todolist.html')
