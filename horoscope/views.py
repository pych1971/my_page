from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

zodiac_dict = {
    'aries': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
    'taurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
    'gemini': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
    'cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
    'leo': ' Лев - пятый знак зодиака, Солнце (с 23 июля по 21 августа).',
    'virgo': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
    'libra': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
    'scorpio': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
    'sagittarius': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
    'capricorn': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
    'aquarius': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
    'pisces': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).'
}

type_dict = {
    'fire': ['aries', 'leo', 'sagittarius'],
    'earth': ['taurus', 'virgo', 'capricorn'],
    'air': ['gemini', 'libra', 'aquarius'],
    'water': ['cancer', 'scorpio', 'pisces']
}

dates_dict = {
    'aries': {3: [21, 31], 4: [1, 20]},
    'taurus': {4: [21, 30], 5: [1, 21]},
    'gemini': {5: [22, 31], 6: [1, 21]},
    'cancer': {6: [22, 30], 7: [1, 22]},
    'leo': {7: [23, 31], 8: [1, 21]},
    'virgo': {8: [22, 31], 9: [1, 23]},
    'libra': {9: [24, 30], 10: [1, 23]},
    'scorpio': {10: [24, 31], 11: [1, 22]},
    'sagittarius': {11: [23, 30], 12: [1, 22]},
    'capricorn': {12: [23, 31], 1: [1, 20]},
    'aquarius': {1: [21, 31], 2: [1, 19]},
    'pisces': {2: [20, 29], 3: [1, 20]}
}

people = [
    {'name': 'Жанна Ивановна Бобылева', 'age': 28, 'phone': '+72609577301'},
    {'name': 'Спиридон Феликсович Алексеев', 'age': 48, 'phone': '8 445 133 42 50'},
    {'name': 'Лыткина Зоя Рубеновна', 'age': 34, 'phone': '84061070300'},
    {'name': 'Олимпиада Святославовна Петухова', 'age': 70, 'phone': '8 740 992 96 95'},
    {'name': 'Лазарева Нина Кирилловна', 'age': 67, 'phone': '89040731989'},
    {'name': 'Каллистрат Ильич Ширяев', 'age': 63, 'phone': '+7 418 298 8976'},
    {'name': 'Евсеев Любосмысл Чеславович', 'age': 47, 'phone': '83111461302'},
    {'name': 'Прохор Харламович Артемьев', 'age': 47, 'phone': '+77827445919'},
    {'name': 'Кондрат Игнатьевич Ершов', 'age': 35, 'phone': '+7 419 594 39 00'},
    {'name': 'Ипат Власович Ильин', 'age': 47, 'phone': '88004779773'}
]


def get_yyyy_converters(request, sign_zodiac):
    return HttpResponse(f'Вы передали число из четырёх цифр - {sign_zodiac}')


def get_my_float_converters(request, sign_zodiac):
    return HttpResponse(f'Вы передали вещественное число - {sign_zodiac}')


def get_me_date_converters(request, sign_zodiac):
    return HttpResponse(f'Вы передали дату - {sign_zodiac}')


def get_my_comma_separated_string(request, sign_zodiac):
    return HttpResponse(f'Вы передали строку - {sign_zodiac}')


def get_my_upper_string(request, sign_zodiac):
    return HttpResponse(f'Ваша строка - {sign_zodiac}')


def index(request):
    zodiacs = list(zodiac_dict)
    # f"<li><a href={redirect_path}>{sign.title()}</a></li>"
    context = {
        'zodiacs': zodiacs,
    }
    return render(request, 'horoscope/index.html', context=context)


def get_list_of_people(request):
    context = {
        'people': people,
    }
    return render(request, 'horoscope/people.html', context=context)

def get_beautiful_table(request):
    return render(request, 'horoscope/beautiful_table.html')

def get_list_of_people_details(request):
    context = {
        'people': people,
    }
    return render(request, 'horoscope/people_detail.html', context=context)


def type(request):
    types = list(type_dict)
    li_elements = ''
    for type_element in types:
        redirect_path = reverse('type-name', args=[type_element])
        li_elements += f"<li><a href={redirect_path}>{type_element.title()}</a></li>"
    response = f"""
    <ol>
        {li_elements}
    </ol>
    """
    return HttpResponse(response)


def get_elements_by_type(request, type_element):
    zodiacs = type_dict[type_element]
    li_elements = ''
    for sign in zodiacs:
        redirect_path = reverse('horoscope-name', args=[sign])
        li_elements += f"<li><a href={redirect_path}>{sign.title()}</a></li>"
    response = f"""
        <ol>
            {li_elements}
        </ol>
        """
    return HttpResponse(response)


def get_info_about_sign_zodiac(request, sign_zodiac: str):
    description = zodiac_dict.get(sign_zodiac)
    data = {
        'description': description,
        'sign': sign_zodiac,
        'zodiacs': zodiac_dict,
    }
    return render(request, 'horoscope/info_zodiac.html', context=data)


def get_info_about_sign_zodiac_by_number(request, sign_zodiac: int):
    zodiacs = list(zodiac_dict)
    if sign_zodiac > len(zodiacs):
        return HttpResponseNotFound(f'Неправильный порядковый номер знака зодиака - {sign_zodiac}')
    name_zodiac = zodiacs[sign_zodiac - 1]
    redirect_url = reverse('horoscope-name', args=[name_zodiac])
    return HttpResponseRedirect(redirect_url)


def get_info_by_date(request, month, day):
    for sign in dates_dict.keys():
        for sign_month in dates_dict[sign].keys():
            if sign_month == month and dates_dict[sign][sign_month][0] <= day <= dates_dict[sign][sign_month][1]:
                redirect_url = reverse('horoscope-name', args=[sign])
                return HttpResponseRedirect(redirect_url)


def get_info_about_Keanu_Reeves(request):
    data = {
        'year_born': 1964,
        'city_born': 'Бейрут',
        'movie_name': 'Мой личный штат Айдахо'
    }
    return render(request, 'horoscope/Keanu_Reeves.html', context=data)


def get_guinness_world_records(request):
    context = {
        'power_man': 'Narve Laeret',
        'bar_name': 'Bob’s BBQ & Grill',
        'count_needle': 1790,
    }
    return render(request, 'horoscope/guinnessworldrecords.html', context=context)
