from django.urls import path
from . import views

urlpatterns = [
    path('',views.get_index),
    path('<int:week_day>', views.get_info_about_week_day_by_number),
    path('<str:week_day>', views.get_info_about_week_day, name='day-name'),
]
