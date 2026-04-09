from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_id):
    return HttpResponse("You are looking at question %s" % question_id)

def result(request, question_id):
    return HttpResponse("You are loking at the result of question %s" % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)