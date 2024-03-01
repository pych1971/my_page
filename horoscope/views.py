from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

zodiac_dict = {
    'aries': "[ɛəri:z] Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).",
    'taurus': "['tɔ:rəs] Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).",
    'gemini': "['dʒeminai] Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).",
    'cancer': "['kænsə(r)] Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).",
    'leo': "['li:əu] Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).",
    'virgo': "['vз:gəu] Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).",
    'libra': "['li:brə] Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).",
    'scorpio': "['skɔ:piəu] Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).",
    'sagittarius': "[sædʒi'tɛəriəs] Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).",
    'capricorn': "['kæprikɔ:n] Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).",
    'aquarius': "['paisi:z] Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).",
    'pisces': "['paisi:z] Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта)."
}


def get_info_about_sign_zodiac(request, sign_zodiac: str):
    description = zodiac_dict.get(sign_zodiac)
    if description:
        return HttpResponse(description)
    else:
        return HttpResponseNotFound(f'Неизвестный знак зодиака - {sign_zodiac}')


def get_info_about_sign_zodiac_by_number(request, sign_zodiac: int):
    return HttpResponse(f'This is number {sign_zodiac}')
