from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def monday(request):
    return HttpResponse("Дела на понедельник")


def tuesday(request):
    return HttpResponse("Дела на вторник")
