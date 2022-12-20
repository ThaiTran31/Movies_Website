from django.shortcuts import render

from rest_framework import generics, permissions

from .serializers import MovieSerializer
from .models import Movie, Category

movies =  [
{
    "name": "Câu Chuyện Cổ Tích",
    "origin_name": "Bir Peri Masalı",
    "description": "<p>Phần trình bày đầu tiên của bộ truyện, nói về sự thay đổi trong cuộc đời của Zeynep (Alina Boz), một cô gái xinh đẹp không biết đọc vì khó khăn tài chính, sau đó chọn làm người trông trẻ. Cha của Zeynep là một người nghiện rượu, nghiện đua ngựa. Zeynep, người tìm thấy rất nhiều tiền vào ngày sinh nhật của cô ấy, sẽ là một thử thách lớn trong cuộc sống giàu có của cô ấy. Loạt phim Bir Peri Masalı, gây tò mò với cả chủ đề và dàn diễn viên thành công, được khán giả háo hức chờ đợi.</p>",
    "type": "series",
    "status": "ongoing",
    "thumb_url": "https://img.ophim.cc/uploads/movies/cau-chuyen-co-tich-thumb.jpg",
    "poster_url": "https://img.ophim.cc/uploads/movies/cau-chuyen-co-tich-poster.jpg",
    "is_copyright": "off",
    "sub_docquyen": "on",
    "chieurap": False,
    "trailer_url": "",
    "time": "2h30p/tập",
    "episode_current": "Tập 2",
    "episode_total": "",
    "quality": "HD",
    "lang": "Vietsub",
    "notify": "",
    "showtimes": "",
    "slug": "cau-chuyen-co-tich",
    "year": 2022,
    "actor": ["Alina Boz", " Taro Emir Tekin", " Tekin Nazan Kesal "],
    "director": ["MERVE ÇOLAK "],
    "category": [
      {
        "name": "Tình Cảm"
      },
      {
        "name": "Tâm Lý"
      }
    ],
    "country": [
      {
        "name": "Thổ Nhĩ Kỳ"
      }
    ]
  },
  {
    "name": "Câu Chuyện Cổ Tích",
    "origin_name": "Bir Peri Masalı",
    "description": "<p>Phần trình bày đầu tiên của bộ truyện, nói về sự thay đổi trong cuộc đời của Zeynep (Alina Boz), một cô gái xinh đẹp không biết đọc vì khó khăn tài chính, sau đó chọn làm người trông trẻ. Cha của Zeynep là một người nghiện rượu, nghiện đua ngựa. Zeynep, người tìm thấy rất nhiều tiền vào ngày sinh nhật của cô ấy, sẽ là một thử thách lớn trong cuộc sống giàu có của cô ấy. Loạt phim Bir Peri Masalı, gây tò mò với cả chủ đề và dàn diễn viên thành công, được khán giả háo hức chờ đợi.</p>",
    "type": "series",
    "status": "ongoing",
    "thumb_url": "https://img.ophim.cc/uploads/movies/cau-chuyen-co-tich-thumb.jpg",
    "poster_url": "https://img.ophim.cc/uploads/movies/cau-chuyen-co-tich-poster.jpg",
    "is_copyright": "off",
    "sub_docquyen": "on",
    "chieurap": False,
    "trailer_url": "",
    "time": "2h30p/tập",
    "episode_current": "Tập 2",
    "episode_total": "",
    "quality": "HD",
    "lang": "Vietsub",
    "notify": "",
    "showtimes": "",
    "slug": "cau-chuyen-co-tich",
    "year": 2022,
    "actor": ["Alina Boz", " Taro Emir Tekin", " Tekin Nazan Kesal "],
    "director": ["MERVE ÇOLAK "],
    "category": [
      {
        "name": "Tình Cảm"
      },
      {
        "name": "Tâm Lý"
      }
    ],
    "country": [
      {
        "name": "Thổ Nhĩ Kỳ"
      }
    ]
  },
]
categories = [
    {
        "name": "Tình Cảm",
        "slug": "tc"
    },
    {
        "name": "Tâm lý",
        "slug": "tl"
    },
    {
        "name": "Hài hước",
        "slug": "hh"
    },
    {
        "name": "Chính kịch",
        "slug": "ck"
    },
    {
        "name": "Gia đình",
        "slug": "gd"
    },
]


class MovieCreate(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()


def MovieListAll(request):
    # movies = Movie.objects.all()
    # categories = Category.objects.all()
    context = {
        'movie_list': movies,
        "categories": categories
    }
    return render(request, 'html/home.html', context=context)


def MovieListByCategory(request, category_slug):
    # category = Category.objects.filter(slug=category_slug)
    # movies_by_cate = category[0].movies.all()
    context = {
        # 'movie_list': movies_by_cate,
        'movies_by_cate': movies,
        "categories": categories
    }
    return render(request, 'html/movie_by_cat.html', context=context)


def MovieDetail(request, movie_slug):
    movie = Movie.objects.get(slug=movie_slug)
    print(movie.query)
    # movie = movies[0]
    context = {
        'movie': movie,
        'category': movie["category"],
        'director': movie["director"],
        'actor': movie["actor"]
    }
    return render(request, 'html/detail.html', context=context)
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
