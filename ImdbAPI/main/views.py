from pkgutil import ImpImporter
from django.shortcuts import get_object_or_404
from .models import Review, WatchList,StreamPlatform
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics,mixins
from .serializers import (
    ReviewSerializer,
    StreamPlatformSerializer,
    WatchListSerializer
)
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


#Created using mixins
# class ReviewListAV(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset=Review.objects.all()
#     serializer_class=ReviewSerializer
    
#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)
    
#     def post(self,request,*args,**kwargs):
#         return self.create(request,*args,**kwargs)
    
# class ReviewDetailAV(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset=Review.objects.all()
#     serializer_class=ReviewSerializer
    
#     def get(self,request,*args,**kwargs):
#         return self.retrieve(request,*args,**kwargs)
# lets create same using Concrete View Classes from generic 


class ReviewListAV(generics.ListAPIView):
    # queryset=Review.objects.all()             #Added get query set so commented
    serializer_class=ReviewSerializer
    
    def get_queryset(self):
        pk= self.kwargs['pk']               # pk for the watchlist whose reviw to show
        return Review.objects.filter(watchlist=pk)
    
class ReviewDetailAV(generics.RetrieveUpdateDestroyAPIView):
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer
    

class ReviewCreateAV(generics.CreateAPIView):
    serializer_class=ReviewSerializer  
    
    def perform_create(self, serializer):
        pk=self.kwargs['pk']
        print(pk)
        watchlist=WatchList.objects.get(id=pk)
        print(watchlist)
        serializer.save(watchlist=watchlist)
        