from rest_framework import serializers
from main.models import Movie


class MovieSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField()
    description=serializers.CharField()
    active=serializers.BooleanField()

    def create(self, validated_data):
       return Movie.objects.create(**validated_data)
    
    # instance -> old values && validated data -> new values  putting new values in old values 
    def update(self, instance, validated_data):
        instance.name=validated_data.get('name')
        instance.description=validated_data.get('description')
        instance.active=validated_data.get('active')
        instance.save()
        return instance  
        