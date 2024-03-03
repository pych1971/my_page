from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

days_dict = {
    'monday': "Дела на понедельник",
    'tuesday': "Дела на вторник",
    'wednesday': "Дела на среду",
    'thursday': "Дела на четверг",
    'friday': "Дела на пятницу",
    'saturday': "Дела на субботу",
    'sunday': "Дела на воскресенье"
}


def get_index(request):
    return render(request, 'week_days/greeting.html')


def get_info_about_week_day(request, week_day):
    description = days_dict.get(week_day)
    if description:
        return HttpResponse(days_dict.get(week_day))
    else:
        return HttpResponseNotFound(f'Неверный день недели - {week_day}')


def get_info_about_week_day_by_number(request, week_day):
    days = list(days_dict)
    if week_day > len(days):
        return HttpResponseNotFound(f'Неверный номер дня - {week_day}')
    day = days[week_day - 1]
    redirect_url = reverse('day-name', args=[day])
    return HttpResponseRedirect(redirect_url)
