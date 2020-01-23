from django.shortcuts import render

from x5quiz.x5gon import search_documents, get_document


def index_view(request):
    return render(request, "quiz/index.html", {})


def search_view(request, query):
    keywords = query.replace(" ", "")

    return render(request, "quiz/search.html", {'keyword': query, 'results': search_documents(query)})


def learn_view(request, document_id):
    return render(request, "quiz/learn.html", {'document': get_document(document_id)})
