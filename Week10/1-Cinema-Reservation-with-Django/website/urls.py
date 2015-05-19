from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^movies/$', views.movies, name='movies'),
    url(r'^movies/(?P<question_id>[0-9]+)/$', views.movie_detail, name='movie_detail')
]
