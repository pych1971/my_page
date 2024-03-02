from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:month>/<int:day>', views.get_info_by_date),
    path('type', views.type),
    path('type/<str:type_element>', views.get_elements_by_type, name='type-name'),
    path('<int:sign_zodiac>', views.get_info_about_sign_zodiac_by_number),
    path('<str:sign_zodiac>', views.get_info_about_sign_zodiac, name='horoscope-name')
]
