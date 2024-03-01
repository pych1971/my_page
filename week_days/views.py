from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.
# def monday(request):
#     return HttpResponse("Дела на понедельник")
#
#
# def tuesday(request):
#     return HttpResponse("Дела на вторник")

def get_info_about_week_day(request, week_day):
    if week_day == 'monday':
        return HttpResponse("Дела на понедельник")
    if week_day == 'tuesday':
        return HttpResponse("Дела на вторник")
    if week_day == 'wednesday':
        return HttpResponse("Дела на среду")
    if week_day == 'thursday':
        return HttpResponse("Дела на четверг")
    if week_day == 'friday':
        return HttpResponse("Дела на пятницу")
    if week_day == 'saturday':
        return HttpResponse("Дела на субботу")
    if week_day == 'sunday':
        return HttpResponse("Дела на воскресенье")
    else:
        return HttpResponseNotFound(f'Не знаю дня недели - {week_day}')
