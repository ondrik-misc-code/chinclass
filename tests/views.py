from django.shortcuts import render
from django.views import generic

from .models import Test
from .models import TaskType
from .models import MultipleChoiceTask
from .models import MCQuestion


class TestView(generic.DetailView):
    model = Test
    template_name = 'tests/test.html'

class TestDetail(generic.DetailView):
    model = Test
    template_name = 'tests/detail.html'

class TestList(generic.ListView):
    model = Test
    context_object_name = 'test_list'
    template_name = 'tests/list.html'

def submit(request, test_id):
    pass
