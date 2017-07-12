from django.conf.urls import url

from . import views

app_name = 'tests'
urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', views.TestView.as_view(), name='test'),
    url(r'^(?P<test_id>[0-9]+)/submit/$', views.submit, name='submit')
]
