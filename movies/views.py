from django.shortcuts import render
from django.db import connection

from rest_framework import generics, permissions

from .serializers import MovieSerializer
from .models import Movie, Category


class MovieCreate(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()

    def post(self, request, *args, **kwargs):
        actor_list = request.data.pop('actors')
        actors = []
        for name in actor_list:
            actor_dict = {"name": name.strip()}
            actors.append(actor_dict)
        director_list = request.data.pop('directors')
        directors = []
        for name in director_list:
            director_dict = {"name": name.strip()}
            directors.append(director_dict)
        request.data.update({"directors": directors, "actors": actors})
        return self.create(request, *args, **kwargs)


def dictfetchall(cursor):
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]


def MovieListAll(request):
    cursor = connection.cursor()
    movies_query = "SELECT * FROM movies_movie;"
    cursor.execute(movies_query)
    movies = dictfetchall(cursor)

    categories_query = "SELECT * FROM movies_category;"
    cursor.execute(categories_query)
    categories = dictfetchall(cursor)

    context = {
        'movie_list': movies,
        "categories": categories
    }
    return render(request, 'html/home.html', context=context)


def MovieListByCategory(request, category_slug):
    cursor = connection.cursor()
    category_query = f'SELECT id FROM movies_category WHERE slug = "{category_slug}"' 
    cursor.execute(category_query)
    category_id = cursor.fetchone()[0]
    movies_by_cate_query = f'SELECT * \
    FROM movies_movie INNER JOIN movies_movie_categories ON (movies_movie.id = movies_movie_categories.movie_id) \
    WHERE movies_movie_categories.category_id = {category_id}'
    cursor.execute(movies_by_cate_query)
    movies_by_cate = dictfetchall(cursor)

    categories_query = "SELECT * FROM movies_category;"
    cursor.execute(categories_query)
    categories = dictfetchall(cursor)

    context = {
        'movies_by_cate': movies_by_cate,
        "categories": categories
    }
    return render(request, 'html/movie_by_cat.html', context=context)


def MovieDetail(request, movie_slug):
    cursor = connection.cursor()
    movie_query = f'SELECT * FROM movies_movie WHERE slug = "{movie_slug}"'
    cursor.execute(movie_query)
    movie = dictfetchall(cursor)[0]
    movie_id = movie.get('id')
    categories = movies_by_cate_query = f'SELECT * \
    FROM movies_movie INNER JOIN movies_movie_categories ON (movies_movie.id = movies_movie_categories.movie_id) \
    WHERE movies_movie_categories.movie_id = {movie_id}'
    print(movie.get('id'))
    print(movie.get('actors'))
    context = {
        'movie': movie,
        'category': movie.get('categories')
    }
    return render(request, 'html/detail.html', context=context)
