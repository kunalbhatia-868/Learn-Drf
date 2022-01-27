from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Movie
# Create your views here.

def movie_list(request):
    movies=Movie.objects.all()
    data={
        'movies':list(movies.values())
    }
    return JsonResponse(data)

def movie_detail(request,pk):
    movie=get_object_or_404(Movie,id=pk)
    data={
        'name':movie.name,
        'description':movie.description,
        'active':movie.active
    }
    return JsonResponse(data)
        