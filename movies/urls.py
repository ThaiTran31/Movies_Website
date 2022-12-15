from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.MovieCreate.as_view(), name='movie-create'),
    path('', views.MovieListAll, name='movie-list'),
    path('movies-by-category/<slug:category_slug>/', views.MovieListByCategory, name='movie-list-by-category'),
    path('<slug:movie_slug>/', views.MovieDetail, name='movie-details'),
    path('', views.home, name='home'),
    path('detail/', views.detail),
]