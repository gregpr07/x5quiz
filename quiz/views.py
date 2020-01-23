from django.shortcuts import render


def index_view(request):
    return render(request, "quiz/index.html", {})


def search_view(request, keyword):
    return render(request, "quiz/search.html", {'keyword': keyword})