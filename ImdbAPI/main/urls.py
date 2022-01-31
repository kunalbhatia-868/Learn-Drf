from django.urls import path
from .views import (
    ReviewListAV,
    ReviewDetailAV,
    WatchListAV,
    WatchListDetailAV,
    StreamPlatformListAV,
    StreamPlatformDetailAV,
)


urlpatterns=[
    path('watchlists/',WatchListAV.as_view(),name="watchlist-list"),
    path('watchlists/<int:pk>',WatchListDetailAV.as_view(),name="watchlist-detail"),
    path('platforms/',StreamPlatformListAV.as_view(),name="platform-list"),
    path('platforms/<int:pk>',StreamPlatformDetailAV.as_view(),name="platform-detail"),
    path('review/',ReviewListAV.as_view(),name="review-list"),
    path('review/<int:pk>',ReviewDetailAV.as_view(),name="review-detail"),
    
]