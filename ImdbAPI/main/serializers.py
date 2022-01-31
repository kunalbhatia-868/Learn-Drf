from rest_framework import serializers
from .models import Review, WatchList,StreamPlatform


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields="__all__"

class WatchListSerializer(serializers.ModelSerializer):
    reviews=ReviewSerializer(many=True,read_only=True)
    class Meta:
        model=WatchList
        fields='__all__'

class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlists=WatchListSerializer(many=True,read_only=True)
    # watchlists=serializers.StringRelatedField(many=True)    #for string name only
    #watchlists = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='watchlist-detail'
    # ) #for hyperlink direct links to the watchlists
    class Meta:
        model=StreamPlatform
        fields='__all__'




