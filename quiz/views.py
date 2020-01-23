from django.shortcuts import render

from x5quiz.errors import search_failed
from x5quiz.x5gon import search_documents, get_document, get_document_content


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
    return render(request, "quiz/learn.html", {'document': get_document(document_id), 'content': get_document_content(document_id)})


def quiz_view(request):
    return render(request, "quiz/quiz.html", {})


def results_view(request):
    return render(request, "quiz/results.html", {})