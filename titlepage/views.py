from django.shortcuts import render
from django.views import generic

from .models import News

# Create your views here.
class TitlePage(generic.ListView):
    model = News
    context_object_name = 'news_list'
    template_name = 'titlepage/index.html'
