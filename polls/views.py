from django.http import Http404, HttpResponse
from polls.models import Question
from django.shortcuts import render

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = "polls/index.html"
    context = {'latest_question_list': latest_question_list}
    
    return render(request, template, context)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    
    template = "polls/detail.html"
    context = {'question': question}
    return render(request, template, context)

def result(request, question_id):
    return HttpResponse("You are loking at the result of question %s" % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)