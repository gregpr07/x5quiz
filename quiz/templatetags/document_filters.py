from django import template

from quiz.models import DocumentStatistics

register = template.Library()


@register.filter(name='star_rating')
def star_rating(document_id, rating):
    buffer = ""
    j = int(rating)
    for i in range(5):
        if j > 0:
            buffer = buffer + '<span class="transparent"><i class="fas fa-star"></i></span>'
        else:
            buffer = buffer + '<span><i class="fas fa-star"></i></span>'
        j -= 1

    return buffer


@register.filter(name='document_title')
def document_title(document_id):
    return DocumentStatistics.objects.get(document_id=document_id).title


@register.filter(name='char_at')
def chat_at(stringu, index):
    return stringu[index*2]