from django import template

from quiz.models import DocumentStatistics

register = template.Library()


@register.filter(name='star_rating')
def star_rating(document_id, rating):
    buffer = ""
    j = int(rating)
    for i in range(5):
        if j > 0:
            buffer = buffer + '<a href="http://localhost:8000/quiz/rate/' + str(document_id) +'/' + str(i+1) + '"><i class="fas fa-star"></i></a>'
        else:
            buffer = buffer + '<a href="http://localhost:8000/quiz/rate/' + str(document_id) +'/' + str(i+1) + ' class="transparent"><i class="fas fa-star"></i></a>'
        j -= 1

    return buffer


@register.filter(name='document_title')
def document_title(document_id):
    return DocumentStatistics.objects.get(document_id=document_id).title


@register.filter(name='char_at')
def chat_at(stringu, index):
    return stringu[index*2]