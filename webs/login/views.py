from django.shortcuts import render,redirect
from .models import login
from django.core.paginator import Paginator
# Create your views here.
# def login(request):
#     context={
#   'login':'Login',
#     } 
#     return render(request,'login.html',context)



def task_list(request):
    tasks = login.objects.all()
    tasks=Paginator(tasks,1)
    return render(request, 'task_list.html', {'taskss': tasks})