from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import (
    ReviewListAV,
    ReviewDetailAV,
    ReviewCreateAV,
    WatchListAV,
    WatchListDetailAV,
    StreamPlatformListAV,
    StreamPlatformDetailAV,
    StreamPlatformViewSetAV
)

router=DefaultRouter()
router.register('platforms',StreamPlatformViewSetAV,basename="streamplatform")

urlpatterns=[
    path('watchlists/',WatchListAV.as_view(),name="watchlist-list"),
    path('watchlists/<int:pk>',WatchListDetailAV.as_view(),name="watchlist-detail"),
    path('',include(router.urls)),
    # path('platforms/',StreamPlatformListAV.as_view(),name="platform-list"),
    # path('platforms/<int:pk>',StreamPlatformDetailAV.as_view(),name="platform-detail"),
    path('watchlists/<int:pk>/review-create/',ReviewCreateAV.as_view(),name="review-create"),
    path('watchlists/<int:pk>/reviews/',ReviewListAV.as_view(),name="review-list"),
    path('watchlists/reviews/<int:pk>',ReviewDetailAV.as_view(),name="review-detail"),
    
]