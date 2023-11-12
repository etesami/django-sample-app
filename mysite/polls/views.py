from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.template import loader
from .forms import NameForm
from .models import Choice, Question
from django.views import generic
from django import forms

# def index(request):
#     # return HttpResponse("Hello, world. You're at the polls index.")
    
#     # We can display the latest questions in the index page:
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
    
#     # Try 0
#     # latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     # output = ', '.join([q.question_text for q in latest_question_list])
#     # return HttpResponse(output)

#     # Try 1
#     # template = loader.get_template('polls/index.html')
#     # context = {
#     #     'latest_question_list': latest_question_list,
#     # }
#     # return HttpResponse(template.render(context, request))

#     # Try 2
#     # An easier approach is to use render
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)
    
    
# def detail(request, question_id):
    
#     # Try 0
#     # return HttpResponse("You're looking at question %s." % question_id)
    
#     # Try 1
#     question = get_object_or_404(Question, pk=question_id)
#     # This is as same as code below:
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exist")
#     return render(request, 'polls/detail.html', {'question': question})

# def results(request, question_id):
#     # response = "You're looking at the results of question %s."
#     # return HttpResponse(response % question_id)
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        # Reverse function helps avoid having to hardcode a URL in the view function. 
        # It is given the name of the view that we want to pass control to and 
        # the variable portion of the URL pattern that points to that view.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
    # return HttpResponse("You're voting on question %s." % question_id)


# The index, detail and results views represent a common case of basic web development: 
# getting data from the database according to a parameter passed in the URL, 
# loading a template and returning the rendered template. Because this is so common, 
# Django provides a shortcut, called the “generic views” system:

# Generic views abstract common patterns to the point where you don’t even 
# need to write Python code to write an app. For example, the ListView and DetailView 
# generic views abstract the concepts of “display a list of objects” and “display a 
# detail page for a particular type of object” respectively.

# Each generic view needs to know what model it will be acting upon.

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    
    # # Try 0
    # # We can provide the model name, then For ListView, the automatically 
    # # generated context variable is question_list. We need to use question_list
    # # in the template
    # model = Question
    
    # Try 1
    # For ListView, the automatically generated context variable is question_list. 
    # To override this we provide the context_object_name attribute, specifying 
    # that we want to use latest_question_list instead.
    context_object_name = 'latest_question_list'
    # by defining the get_queryset we specify the model the view is acting upon
    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

    
    
    
# # class MyForm(forms.Form):
# #     template_name = "polls/name.html"    
    
    
def get_name(request):
    # form = MyForm()
    # rendered_form = form.render("polls/name.html")
    # context = {'form': rendered_form}
    # return render(request, 'polls/thanks.html', context)
    
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            your_name = form.cleaned_data['your_name']
            context = {'your_name': your_name}
            return render(request, 'polls/thanks.html', context)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
    return render(request, 'polls/name.html', {'form': form})
