from django.shortcuts import render

from quiz.models import DocumentStatistics, Quiz, QuizUserResult
from x5quiz.errors import search_failed, submission_failed
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


def quiz_submit_view(request, quiz_pk):
    print(request.POST)

    quiz = Quiz.objects.get(pk=quiz_pk)
    correct = 0
    buffer = ""

    for element in request.POST:
        if element == "csrfmiddlewaretoken": continue
        question = quiz.get_quiz_question(int(element[0])-1)
        print("question.text: " + question.text)
        print("question.correct: " + str(question.correct))
        print("passed: ", int(element[2])-1)
        buffer = buffer + str(int(element[2])-1) + "-"
        if question.correct == int(element[2])-1:
            correct = correct + 1

    wrong = quiz.get_quiz_questions().count() - correct

    results = QuizUserResult.objects.create(quiz=quiz, user=request.user, correct=correct, wrong=wrong, data=buffer[:-1])
    results.save()

    return render(request, "quiz/results.html", {
        'quiz': quiz,
        'results': results,
        'data': buffer[:-1],
        'leaderboard': QuizUserResult.objects.filter(quiz=quiz).order_by("-correct")
    })