from django import template

register = template.Library()


@register.filter(name='times')
def times(value):
    return list(i for i in range(value))


@register.filter(name='filter_range')
def filter_range(value1, value2):
    return list(i for i in range(value1, value2))
