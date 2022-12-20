from django.shortcuts import render
from django.db import connection

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
# Create your views here.
def home(request):
    context = {
        'tabs': ['Home', 'Movies', 'Web Series', 'Kids','TV', 'Premium'],   
        'movies': [
            {
                'brand': 'Ford',
                'model': 'Mustang',
                'year': '1964',
            },
            {
                'brand': 'Ford',
                'model': 'Bronco',
                'year': '1970',
            },
            {
                'brand': 'Ford',
                'model': 'Bronco',
                'year': '1970',
            },
            {
                'brand': 'Ford',
                'model': 'Bronco',
                'year': '1970',
            },
            {
                'brand': 'Ford',
                'model': 'Bronco',
                'year': '1970',
            },
            {
                'brand': 'Ford',
                'model': 'Bronco',
                'year': '1970',
            },
            {
                'brand': 'Volvo',
                'model': 'P1800',
                'year': '1964',
            }
        ]
    }
    return render(request, "html/home.html", context=context)

def detail(request):
    context = {}
    return render(request, "html/detail.html", context=context)
