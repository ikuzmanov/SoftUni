from django.shortcuts import render, HttpResponse, get_object_or_404, get_list_or_404

# Create your views here.
from polls.models import Question


def index(request):
    latest_question_list = get_list_or_404(Question)
    template = 'polls/index.html'
    context = {'latest_question_list': latest_question_list}
    return render(request, template, context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    template = 'polls/detail.html'
    context = {'question': question}
    return render(request, template, context)


def results(request, question_id):
    return HttpResponse(f"You're looking at the results of question {question_id}.")


def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}.")
