from django.shortcuts import render
from .models import Movie, Projection


def index(request):
    title = 'Cinema'
    movies = Movie.objects.all()[:3]
    return render(request, 'index.html', locals())


def movies(request):
    movies = Movie.objects.all()
    title = 'All movies'
    return render(request, 'movies.html', locals())


def movie_detail(request, question_id):
    projections = Projection.objects.filter(movie_id_id=question_id)
    movie = Movie.objects.get(id=question_id)
    title = movie.name
    return render(request, 'detail_movie.html', locals())
