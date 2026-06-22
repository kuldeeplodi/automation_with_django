from django.shortcuts import render
from django.http import HttpResponse
from dataentry.task import celery_task_test


def home(request):
    return render(request,'home.html')


def celery_test(request):
    celery_task_test.delay()
    return HttpResponse("<h1>function executed successfully</h1>")
     