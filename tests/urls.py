from django.conf.urls import url

from . import views

app_name = 'tests'
urlpatterns = [
    url(r'^$', views.TestList.as_view(), name='list'),
    url(r'^(?P<pk>[0-9]+)/take$', views.TestView.as_view(), name='test'),
    url(r'^(?P<pk>[0-9]+)/detail$', views.TestDetail.as_view(), name='detail'),
    url(r'^(?P<test_id>[0-9]+)/submit/$', views.submit_test, name='submit_test'),
    url(r'^results/(?P<pk>[0-9]+)/$', views.TestResults.as_view(), name='test_results'),
]
