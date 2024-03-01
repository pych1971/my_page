from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.
# def aries(request):
#     return HttpResponse("[ɛəri:z] Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).")
#
#
# def taurus(request):
#     return HttpResponse("['tɔ:rəs] Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).")
#
#
# def gemini(request):
#     return HttpResponse("['dʒeminai] Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).")
#
#
# def cancer(request):
#     return HttpResponse("['kænsə(r)] Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).")
#
#
# def leo(request):
#     return HttpResponse("['li:əu] Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).")
#
#
# def virgo(request):
#     return HttpResponse("['vз:gəu] Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).")
#
#
# def libra(request):
#     return HttpResponse("['li:brə] Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).")
#
#
# def scorpio(request):
#     return HttpResponse("['skɔ:piəu] Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).")
#
#
# def sagittarius(request):
#     return HttpResponse("[sædʒi'tɛəriəs] Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).")
#
#
# def capricorn(request):
#     return HttpResponse("['kæprikɔ:n] Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).")
#
#
# def aquarius(request):
#     return HttpResponse(
#         "[ə'kwɛəriəs] Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).")
#
#
# def pisces(request):
#     return HttpResponse("['paisi:z] Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).")


def get_info_about_sign_zodiac(request, sign_zodiac):
    if sign_zodiac == 'aries':
        return HttpResponse("[ɛəri:z] Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).")
    if sign_zodiac == 'taurus':
        return HttpResponse("['tɔ:rəs] Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).")
    if sign_zodiac == 'gemini':
        return HttpResponse("['dʒeminai] Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).")
    if sign_zodiac == 'cancer':
        return HttpResponse("['kænsə(r)] Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).")
    if sign_zodiac == 'leo':
        return HttpResponse("['li:əu] Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).")
    if sign_zodiac == 'virgo':
        return HttpResponse("['vз:gəu] Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).")
    if sign_zodiac == 'libra':
        return HttpResponse("['li:brə] Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).")
    if sign_zodiac == 'scorpio':
        return HttpResponse("['skɔ:piəu] Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).")
    if sign_zodiac == 'sagittarius':
        return HttpResponse(
            "[sædʒi'tɛəriəs] Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).")
    if sign_zodiac == 'capricorn':
        return HttpResponse("['kæprikɔ:n] Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).")
    if sign_zodiac == 'aquarius':
        return HttpResponse("['paisi:z] Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).")
    if sign_zodiac == 'pisces':
        return HttpResponse("['paisi:z] Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).")
    else:
        return HttpResponseNotFound(f'Неизвестный знак зодиака - {sign_zodiac}')
