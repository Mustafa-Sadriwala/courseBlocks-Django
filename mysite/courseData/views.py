from django.http import HttpResponse
from django.template import loader

from .models import Course

def all(request):
    latest_question_list = Course.objects.order_by('subj')[:5]
    template = loader.get_template('courseData.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def subj(request):
    latest_question_list = Course.objects.order_by('class_num')[:5]
    template = loader.get_template('courseData/subj.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def course_data(request, subj, course_num):
    return HttpResponse("You're looking at %s %s." % subj % course_num)

'''def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)'''

# Create your views here.
