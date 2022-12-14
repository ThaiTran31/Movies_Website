from django.shortcuts import render

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