from django.urls import path, register_converter
from . import views, converters

register_converter(converters.FourDigitYearConverter, "yyyy")
register_converter(converters.MyFloatConverter, "my_float")
register_converter(converters.MyDateConverter, "my_date")
register_converter(converters.SplitConverter, "my_comma_separated_string")

urlpatterns = [
    path('', views.index),
    path('<int:month>/<int:day>', views.get_info_by_date),
    path('type', views.type),
    path('type/<str:type_element>', views.get_elements_by_type, name='type-name'),
    path('<my_comma_separated_string:sign_zodiac>', views.get_my_comma_separated_string),
    path('<my_date:sign_zodiac>', views.get_me_date_converters),
    path('<yyyy:sign_zodiac>', views.get_yyyy_converters),
    path('<int:sign_zodiac>', views.get_info_about_sign_zodiac_by_number),
    path('<my_float:sign_zodiac>', views.get_my_float_converters),
    path('<str:sign_zodiac>', views.get_info_about_sign_zodiac, name='horoscope-name')
]
