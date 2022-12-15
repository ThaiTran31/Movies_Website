from django.shortcuts import render

from rest_framework import generics, permissions

from .serializers import MovieSerializer
from .models import Movie, Category


class MovieCreate(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()


def MovieListAll(request):
    movies = Movie.objects.all()
    context = {
        'movie_list': movies,
    }
    return render(request, 'movie_list.html', context=context)


def MovieListByCategory(request, category_slug):
    category = Category.objects.filter(slug=category_slug)
    movies_by_cate = category[0].movies.all()
    context = {
        'movie_list': movies_by_cate,
    }
    return render(request, 'movie_list.html', context=context)


def MovieDetail(request, movie_slug):
    movie = Movie.objects.get(slug=movie_slug)
    context = {
        'movie': movie,
    }
    return render(request, 'movie_details.html', context=context)
