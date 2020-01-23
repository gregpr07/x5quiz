from django import template

register = template.Library()


@register.filter(name='star_rating')
def star_rating(rating):
    buffer = ""
    for i in range(int(rating)):
        buffer = buffer + '<span><i class="fas fa-star"></i></span>'

    return buffer
