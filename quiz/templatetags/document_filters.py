from django import template

from x5quiz.x5gon import get_document

register = template.Library()


@register.filter(name='star_rating')
def star_rating(rating):
    buffer = ""
    for i in range(int(rating)):
        buffer = buffer + '<span><i class="fas fa-star"></i></span>'

    return buffer


@register.filter(name='document_title')
def document_title(document_id):
    return get_document(document_id)['title']


@register.filter(name='char_at')
def chat_at(stringu, index):
    return stringu[index*2]