from django.shortcuts import render

from quiz.models import DocumentStatistics, Quiz
from x5quiz.errors import search_failed
from x5quiz.x5gon import search_documents, get_document, get_document_content, generate_document_questions, \
    get_document_url


def index_view(request):
    return render(request, "quiz/index.html", {})


def search_view(request):
    query = None
    if request.method == 'POST':
        query = request.POST['query']

    if query is None or len(query) < 2:
        return search_failed(request)

    query = query.replace(" ", "")
    return render(request, "quiz/search.html", {'keyword': query, 'results': search_documents(query)})


def learn_view(request, document_id):
    statistics = None

    if not DocumentStatistics.objects.filter(document_id=document_id).exists():
        statistics = DocumentStatistics.objects.create(document_id=document_id, views=1)
    else:
        statistics = DocumentStatistics.objects.get(document_id=document_id)
        statistics.increase_views()

    return render(request, "quiz/learn.html", {
        'document': get_document(document_id),
        'content': get_document_content(document_id),
        'url': get_document_url(document_id),
        'statistics': statistics,
    })


def quiz_view(request, document_id):
    questions = generate_document_questions(document_id)

    return render(request, "quiz/quiz.html", {
        'document': get_document(document_id),
        'content': get_document_content(document_id),
        'quiz': Quiz.objects.get(document_id=document_id),
    })


def results_view(request):
    return render(request, "quiz/results.html", {})