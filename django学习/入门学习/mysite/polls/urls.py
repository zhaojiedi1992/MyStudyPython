from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView),
    url(r'^(?P<question_id>[0-9]+)/$',views.DetailView),
    url(r'^(?P<question_id>[0-9]+)/results/$',views.ResultsView),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote),
]