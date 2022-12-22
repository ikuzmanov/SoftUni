from django.template import Library

register = Library()


@register.filter(name='odd')
def get_odd(values):
    return tuple(int(num) for num in values if num % 2 == 1)


@register.filter(name='starify')
def add_stars_in_sequence(words):
    return "".join(tuple([word + "*" for word in words]))
