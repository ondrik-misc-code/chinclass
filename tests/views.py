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

###########################################
def submit_test(request, test_id):
    test = get_object_or_404(Test, pk=test_id)

    subm_test = SubmTest()
    subm_test.test = test
    subm_test.student_name = request.POST['stud_name']
    subm_test.save()

    # add task submissions
    for mctask in test.mctask_set.all():
        subm_mctask = SubmMCTask()
        subm_mctask.subm_test = subm_test
        subm_mctask.task = mctask
        subm_mctask.save()

    return HttpResponseRedirect(reverse('tests:test_results',
        args=(subm_test.id,)))

###########################################
class TestResults(generic.DetailView):
    model = SubmTest
    context_object_name = 'subm'
    template_name = 'tests/test_results.html'
