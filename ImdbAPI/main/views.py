from django.shortcuts import get_object_or_404
from .models import WatchList,StreamPlatform
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import StreamPlatformSerializer, WatchListSerializer
# Create your views here.

class WatchListAV(APIView):
    
    def get(self,request):
        watchlists=WatchList.objects.all()
        serializer=WatchListSerializer(watchlists,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer=WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
        
class WatchListDetailAV(APIView):
    
    def get(self,request,pk):
        watchlist=get_object_or_404(WatchList,id=pk)
        serializer=WatchListSerializer(watchlist)
        return Response(serializer.data,status=status.HTTP_200_OK)      
    
    def put(self,request,pk):
        watchlist=get_object_or_404(WatchList,id=pk)
        serializer=WatchListSerializer(watchlist,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,pk):
        watchlist=get_object_or_404(WatchList,id=pk)
        watchlist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class StreamPlatformListAV(APIView):
    def get(self,request):
        platforms=StreamPlatform.objects.all()
        serializer=StreamPlatformSerializer(platforms,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)    
    
    def post(self,request):
        serializer=StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)        
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
class StreamPlatformDetailAV(APIView):
    def get(self,request,pk):
        platform=get_object_or_404(StreamPlatform,id=pk)
        serializer=StreamPlatformSerializer(platform)
        return Response(serializer.data,status=status.HTTP_200_OK)      
    
    def put(self,request,pk):
        platform=get_object_or_404(StreamPlatform,id=pk)
        serializer=StreamPlatformSerializer(platform,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,pk):
        platform=get_object_or_404(StreamPlatform,id=pk)
        platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
                