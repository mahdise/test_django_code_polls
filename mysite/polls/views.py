from .models import Question, Choices
from django.shortcuts import render,get_object_or_404
from django.http import  HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def index(request):
    latest_questions= Question.objects.order_by('-pub_date')[:5]
    # template= loader.get_template('polls/index.html')
    # context= RequestContext(request,{'latest_question': latest_questions})
    context= {'latest_question': latest_questions}
    return render(request, 'polls/index.html',context)


# function of flatten return the result as a dict
def detail(request, question_id):
    question= get_object_or_404(Question, pk=question_id)
    return render(request,'polls/detail.html',{'question':question})



def results(request,question_id):
    question= get_object_or_404(Question, pk=question_id)
    return render(request,'polls/results.html',{'question': question})

def vote(request, question_id):
    question=get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choices_set.get(pk=request.POST['choices'])


    # except:
        # return render(request,'polls/detail.html', {'question': question, 'error_message':"Please select a choice------"})
    except (KeyError, Choices.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results', args= (question.id, )))


