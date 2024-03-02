from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


# Create your views here.

def get_rectangle_area(request, width, height):
    return HttpResponse(f"Площадь прямоугольника размером {width}x{height} равна {width * height}")


def get_rectangle_area_redirect(request, width, height):
    redirect_url = reverse('rectangle-name', args=[width, height])
    return HttpResponseRedirect(redirect_url)


def get_square_area(request, width):
    return HttpResponse(f"Площадь квадрата размером {width}x{width} равна {width ** 2}")


def get_square_area_redirect(request, width):
    redirect_url = reverse('square-name', args=[width])
    return HttpResponseRedirect(redirect_url)


def get_circle_area(request, radius):
    return HttpResponse(f"Площадь круга с радиусом {radius} равна {3.14 * radius ** 2}")


def get_circle_area_redirect(request, radius):
    redirect_url = reverse('circle-name', args=[radius])
    return HttpResponseRedirect(redirect_url)
