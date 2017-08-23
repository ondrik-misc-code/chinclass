from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

# from .models import Test
# from .models import TaskType
# from .models import MCTask
# from .models import MCQuestion
# from .models import SubmTest
# from .models import SubmTask
from .models import *


###########################################
class TestView(generic.DetailView):
    model = Test
    template_name = 'tests/test.html'

###########################################
class TestDetail(generic.DetailView):
    model = Test
    template_name = 'tests/detail.html'

###########################################
class TestList(generic.ListView):
    model = Test
    context_object_name = 'test_list'
    template_name = 'tests/list.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(TestList, self).get_context_data(**kwargs)
        # Add in a QuerySet some more
        context['subm_list'] = SubmTest.objects.all()
        return context

###########################################
def submit_test(request, test_id):
    '''submit_test(request, test_id)

Submits a test solution and redirects to the result.
'''
    test = get_object_or_404(Test, pk=test_id)

    subm_test = SubmTest()
    subm_test.test = test
    subm_test.student_name = request.POST.get('stud_name')
    subm_test.save()

    # add all MC task submissions
    for mctask in test.mctask_set.all():
        for mcquest in mctask.mcquestion_set.all():
            subm_mcquest = SubmMCQuestion()
            subm_mcquest.subm_test = subm_test
            subm_mcquest.mcquest = mcquest

            # process the answer
            subm_choice_id = request.POST.get('mcquest:' + str(mcquest.id))
            try:
                subm_choice = mcquest.mcquestionchoice_set.get(pk=subm_choice_id)
            except (KeyError, MCQuestionChoice.DoesNotExist):
                pass
            else:
                subm_mcquest.mcquestchoice = subm_choice

            subm_mcquest.save()
            print(subm_mcquest)

    return HttpResponseRedirect(reverse('tests:test_results',
        args=(subm_test.id,)))

###########################################
class TestResults(generic.DetailView):
    model = SubmTest
    context_object_name = 'subm'
    template_name = 'tests/test_results.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(TestResults, self).get_context_data(**kwargs)
        # Add in a QuerySet some more
        subm = context['subm']
        mcquest_subm_all = subm.submmcquestion_set.all()
        context['mcquest_subm'] = [mcquest_subm.mcquestchoice.id \
            for mcquest_subm in mcquest_subm_all \
            if mcquest_subm.mcquestchoice != None]
        context['correctly_answered_mcquest'] = [ mcquest_subm.mcquest.id \
            for mcquest_subm in mcquest_subm_all
            if mcquest_subm.correct ]

        scores_mctask = { }
        for mctask in subm.test.mctask_set.all():
            scores_mctask[mctask.id] = mctask.score_for(subm)

        context['scores_mctask'] = scores_mctask
        return context
