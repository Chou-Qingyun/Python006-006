from django import template

register = template.Library()

@register.filter

def split_space(value):
    return value.split(' ')[0]