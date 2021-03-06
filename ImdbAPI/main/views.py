from django.shortcuts import get_object_or_404
from .pagination import WatchListCPagination, WatchListPagination,WatchListLimitOffsetPagination
from .models import Review, WatchList,StreamPlatform
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics,mixins,viewsets
from .serializers import (
    ReviewSerializer,
    StreamPlatformSerializer,
    WatchListSerializer
)
from.permissions import IsAdminOrReadOnly, IsReviewOwnerOrReadOnly
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.throttling import UserRateThrottle,AnonRateThrottle
from .throttling import ReviewCreateThrottle,ReviewListThrottle
from rest_framework.throttling import ScopedRateThrottle
# Create your views here.

#implementing url filtering
class UserReview(generics.ListAPIView):
    serializer_class=ReviewSerializer
    # throttle_classes=[ReviewListThrottle,AnonRateThrottle] 

    # def get_queryset(self):
    #     username=self.kwargs['username']
    #     return Review.objects.filter(review_user__username=username)
    # Filtering Against URL
    
    def get_queryset(self):
        username=self.request.query_params.get('username',None)
        return Review.objects.filter(review_user__username=username)
        
    
    # Filtering against query parameter
    
class WatchListAV(APIView):
    permission_classes=[IsAdminOrReadOnly]
    pagination_class=WatchListPagination    #Will Not Work on API Vie only for generic classes
    
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
    permission_classes = [IsAdminOrReadOnly]
    
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
    
#Helps define all the list detail create view under only one view and handled using routers
#no need to create multiple urls as well
#Not Recoommended with simple requirements ,can be used in complex projects to decrease size of code
# class StreamPlatformViewSetAV(viewsets.ViewSet):
#     def list(self, request):
#         queryset = StreamPlatform.objects.all()
#         serializer = StreamPlatformSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         queryset = StreamPlatform.objects.all()
#         user = get_object_or_404(queryset, pk=pk)
#         serializer = StreamPlatformSerializer(user)
#         return Response(serializer.data)
    
#     def create(self,request):
#         serializer=StreamPlatformSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)        
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#For ModelViewSet
# all methof get post patch and delete in 3 lines of code

class StreamPlatformViewSetAV(viewsets.ModelViewSet):
    queryset=StreamPlatform.objects.all()
    serializer_class=StreamPlatformSerializer
    permission_classes = [IsAdminOrReadOnly]
# User viewsets.ReadonlyView set for only get permission

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
    permission_classes = [IsAdminOrReadOnly]
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
    # permission_classes=[IsAuthenticatedOrReadOnly]    #Inbuild Permission Classes
    # permission_classes=[IsAuthenticated]            #Custom Permission class
    # throttle_classes=[UserRateThrottle,AnonRateThrottle]
    throttle_classes=[ReviewListThrottle]#for scope throttle    
    filter_backends=[DjangoFilterBackend]
    filterset_fields=['review_user__username','active']
    # for generic filtering
    
    def get_queryset(self):
        pk= self.kwargs['pk']               # pk for the watchlist whose reviw to show
        return Review.objects.filter(watchlist=pk)
    
class ReviewDetailAV(generics.RetrieveUpdateDestroyAPIView):
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer
    permission_classes=[IsReviewOwnerOrReadOnly]
    # throttle_classes=[UserRateThrottle,AnonRateThrottle]
    throttle_classes=[ScopedRateThrottle]
    throttle_scope='review-detail'          #dd scope for thottle in views only and define the rate in seetings.py
    
class ReviewCreateAV(generics.CreateAPIView):
    serializer_class=ReviewSerializer  
    permission_classes = [IsAuthenticated]
    throttle_classes=[ReviewCreateThrottle]#for scope throttle    

    def get_queryset(self):
        return Review.objects.all()
    
    def perform_create(self, serializer):
        pk=self.kwargs['pk']
        watchlist=WatchList.objects.get(id=pk)
        review_user=self.request.user
        review_qs=Review.objects.filter(review_user=review_user,watchlist=watchlist)
        if review_qs.exists():
            raise ValidationError("You have already review this movie")
        else:
            if watchlist.number_rating==0:
                watchlist.avg_rating=serializer.validated_data['rating']
            else:
                watchlist.avg_rating=(watchlist.avg_rating+serializer.validated_data['rating'])/2
            watchlist.number_rating+=1
            watchlist.save()
            serializer.save(watchlist=watchlist,review_user=review_user)
            
# To test out search with filtering
class WatchListSearch(generics.ListAPIView):
    queryset=WatchList.objects.all()
    serializer_class=WatchListSerializer
    # throttle_classes=[ReviewListThrottle]
    # filter_backends=[DjangoFilterBackend]
    # filter_backends=[SearchFilter]#for search filter
    # search_fields_fields=['title','platform__name']
    # filter_backends=[OrderingFilter]
    # ordering_fields=['avg_rating']
    pagination_class=WatchListCPagination