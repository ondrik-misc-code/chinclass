from django.conf.urls import url

from . import views

app_name = 'titlepage'
urlpatterns = [
    url(r'^$', views.TitlePage.as_view(), name='titlepage'),
]
