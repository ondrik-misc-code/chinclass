from django.shortcuts import render
from django.views import generic

from .models import Test
from .models import TaskType
from .models import MultipleChoiceTask
from .models import MCQuestion


class TestView(generic.DetailView):
    model = Test
    template_name = 'tests/test.html'

def submit(request, test_id):
    pass
