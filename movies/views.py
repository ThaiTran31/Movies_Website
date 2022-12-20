from django.shortcuts import render
from django.db import connection

from rest_framework import generics, permissions

from .serializers import MovieSerializer
from .models import Movie, Category

# movies =  [
# {
#     "name": "Câu Chuyện Cổ Tích",
#     "origin_name": "Bir Peri Masalı",
#     "description": "<p>Phần trình bày đầu tiên của bộ truyện, nói về sự thay đổi trong cuộc đời của Zeynep (Alina Boz), một cô gái xinh đẹp không biết đọc vì khó khăn tài chính, sau đó chọn làm người trông trẻ. Cha của Zeynep là một người nghiện rượu, nghiện đua ngựa. Zeynep, người tìm thấy rất nhiều tiền vào ngày sinh nhật của cô ấy, sẽ là một thử thách lớn trong cuộc sống giàu có của cô ấy. Loạt phim Bir Peri Masalı, gây tò mò với cả chủ đề và dàn diễn viên thành công, được khán giả háo hức chờ đợi.</p>",
#     "type": "series",
#     "status": "ongoing",
#     "thumb_url": "https://img.ophim.cc/uploads/movies/cau-chuyen-co-tich-thumb.jpg",
#     "poster_url": "https://img.ophim.cc/uploads/movies/cau-chuyen-co-tich-poster.jpg",
#     "is_copyright": "off",
#     "sub_docquyen": "on",
#     "chieurap": False,
#     "trailer_url": "",
#     "time": "2h30p/tập",
#     "episode_current": "Tập 2",
#     "episode_total": "",
#     "quality": "HD",
#     "lang": "Vietsub",
#     "notify": "",
#     "showtimes": "",
#     "slug": "cau-chuyen-co-tich",
#     "year": 2022,
#     "actor": ["Alina Boz", " Taro Emir Tekin", " Tekin Nazan Kesal "],
#     "director": ["MERVE ÇOLAK "],
#     "category": [
#       {
#         "name": "Tình Cảm"
#       },
#       {
#         "name": "Tâm Lý"
#       }
#     ],
#     "country": [
#       {
#         "name": "Thổ Nhĩ Kỳ"
#       }
#     ]
#   },
#   {
#     "name": "Câu Chuyện Cổ Tích",
#     "origin_name": "Bir Peri Masalı",
#     "description": "<p>Phần trình bày đầu tiên của bộ truyện, nói về sự thay đổi trong cuộc đời của Zeynep (Alina Boz), một cô gái xinh đẹp không biết đọc vì khó khăn tài chính, sau đó chọn làm người trông trẻ. Cha của Zeynep là một người nghiện rượu, nghiện đua ngựa. Zeynep, người tìm thấy rất nhiều tiền vào ngày sinh nhật của cô ấy, sẽ là một thử thách lớn trong cuộc sống giàu có của cô ấy. Loạt phim Bir Peri Masalı, gây tò mò với cả chủ đề và dàn diễn viên thành công, được khán giả háo hức chờ đợi.</p>",
#     "type": "series",
#     "status": "ongoing",
#     "thumb_url": "https://img.ophim.cc/uploads/movies/cau-chuyen-co-tich-thumb.jpg",
#     "poster_url": "https://img.ophim.cc/uploads/movies/cau-chuyen-co-tich-poster.jpg",
#     "is_copyright": "off",
#     "sub_docquyen": "on",
#     "chieurap": False,
#     "trailer_url": "",
#     "time": "2h30p/tập",
#     "episode_current": "Tập 2",
#     "episode_total": "",
#     "quality": "HD",
#     "lang": "Vietsub",
#     "notify": "",
#     "showtimes": "",
#     "slug": "cau-chuyen-co-tich",
#     "year": 2022,
#     "actor": ["Alina Boz", " Taro Emir Tekin", " Tekin Nazan Kesal "],
#     "director": ["MERVE ÇOLAK "],
#     "category": [
#       {
#         "name": "Tình Cảm"
#       },
#       {
#         "name": "Tâm Lý"
#       }
#     ],
#     "country": [
#       {
#         "name": "Thổ Nhĩ Kỳ"
#       }
#     ]
#   },
# ]
# categories = [
#     {
#         "name": "Tình Cảm",
#         "slug": "tc"
#     },
#     {
#         "name": "Tâm lý",
#         "slug": "tl"
#     },
#     {
#         "name": "Hài hước",
#         "slug": "hh"
#     },
#     {
#         "name": "Chính kịch",
#         "slug": "ck"
#     },
#     {
#         "name": "Gia đình",
#         "slug": "gd"
#     },
# ]


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
    # print(connection.queries)

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
    # movie = Movie.objects.get(slug=movie_slug)
    movie = movies[0]
    context = {
        'movie': movie,
        'category': movie["category"],
        'director': movie["director"],
        'actor': movie["actor"]
    }
    return render(request, 'html/detail.html', context=context)
# Create your views here.
# def home(request):
#     context = {
#         'tabs': ['Home', 'Movies', 'Web Series', 'Kids','TV', 'Premium'],   
#         'movies': [
#             {
#                 'brand': 'Ford',
#                 'model': 'Mustang',
#                 'year': '1964',
#             },
#             {
#                 'brand': 'Ford',
#                 'model': 'Bronco',
#                 'year': '1970',
#             },
#             {
#                 'brand': 'Ford',
#                 'model': 'Bronco',
#                 'year': '1970',
#             },
#             {
#                 'brand': 'Ford',
#                 'model': 'Bronco',
#                 'year': '1970',
#             },
#             {
#                 'brand': 'Ford',
#                 'model': 'Bronco',
#                 'year': '1970',
#             },
#             {
#                 'brand': 'Ford',
#                 'model': 'Bronco',
#                 'year': '1970',
#             },
#             {
#                 'brand': 'Volvo',
#                 'model': 'P1800',
#                 'year': '1964',
#             }
#         ]
#     }
#     return render(request, "html/home.html", context=context)

# def detail(request):
#     context = {}
#     return render(request, "html/detail.html", context=context)
