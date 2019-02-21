from django.shortcuts import render
from django.template import loader
# Create your views here.
from django.http import HttpResponse
from .models import Question
#commentar test 21.09.2019 16:10
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #output = ', '.join([q.question_text for q in latest_question_list])
	### Content of index.html loaded into Var template ###
    template = loader.get_template('polls/index.html')
	### the context  look for the first string (left) in the template and consider it as the second variable (right side)###
    context = {
	     'latest_question_listaa' : latest_question_list,
	}
    return HttpResponse(template.render(context,request))

def detail(request, question_id):
    return HttpResponse("You are looking for Quenstion %s ." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def votetest(request):
    return HttpResponse("Hello, Wolrd. You'are at the Polls testtttttttttt index. ")