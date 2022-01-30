from django.urls import path
from .views import (
    WatchListAV,
    WatchListDetailAV,
    StreamPlatformListAV,
    StreamPlatformDetailAV,
)


urlpatterns=[
    path('watchlists/',WatchListAV.as_view(),name="watchlists"),
    path('watchlists/<int:pk>',WatchListDetailAV.as_view(),name="watchlist-detail"),
    path('platforms/',StreamPlatformListAV.as_view(),name="platforms"),
    path('platforms/<int:pk>',StreamPlatformDetailAV.as_view(),name="platform-detail"),
]