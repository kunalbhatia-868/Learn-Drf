from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from main.models import Movie
from .serializers import MovieSerializer
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.
# Function Based Views
# @api_view(['GET','POST'])
# def movie_list(request):
#     if request.method =='GET':        
#         movies=Movie.objects.all()
#         serializer=MovieSerializer(movies,many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)
    
#     if request.method=="POST":
#         serializer=MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

# @api_view(['GET','PUT','DELETE'])
# def movie_detail(request,pk):
#     if request.method=="GET":
#         movie=get_object_or_404(Movie,id=pk)
#         serializer=MovieSerializer(movie)
#         return Response(serializer.data,status=status.HTTP_200_OK)
    
#     if request.method=="PUT":
#         movie=get_object_or_404(Movie,id=pk)
#         serializer=MovieSerializer(movie,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)    
    
#     if request.method=="DELETE":
#         movie=get_object_or_404(Movie,id=pk)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
        

# Class Based Views  with same function as above just instead of if statement we use the given functions

class MovieListAV(APIView):
    
    def get(self,request):
        movies=Movie.objects.all()
        serializer=MovieSerializer(movies,many=True)
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
    def post(self,request):
        serializer=MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
        
class MovieDetailAV(APIView):
    
    def get(self,request,pk):
        movie=get_object_or_404(Movie,id=pk)
        serializer=MovieSerializer(movie)
        return Response(serializer.data,status=status.HTTP_200_OK)      
    
    def put(self,request,pk):
        movie=get_object_or_404(Movie,id=pk)
        serializer=MovieSerializer(movie,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,pk):
        movie=get_object_or_404(Movie,id=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)   