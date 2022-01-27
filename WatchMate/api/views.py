from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from main.models import Movie
from .serializers import MovieSerializer

# Create your views here.
@api_view(['GET','POST'])
def movie_list(request):
    if request.method =='GET':        
        movies=Movie.objects.all()
        serializer=MovieSerializer(movies,many=True)
        return Response(serializer.data)
    
    if request.method=="POST":
        serializer=MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return serializer.errors()
        

@api_view(['GET','PUT','DELETE'])
def movie_detail(request,pk):
    if request.method=="GET":
        movie=get_object_or_404(Movie,id=pk)
        serializer=MovieSerializer(movie)
        return Response(serializer.data)
    
    if request.method=="PUT":
        movie=get_object_or_404(Movie,id=pk)
        serializer=MovieSerializer(movie,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)    
    
    if request.method=="DELETE":
        movie=get_object_or_404(Movie,id=pk)
        movie.delete()
        return HttpResponse("deleted")
        
        
    