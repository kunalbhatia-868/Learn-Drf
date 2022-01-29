from rest_framework import serializers

def check_length(value):
    if(len(value)<5):
        raise serializers.ValidationError("Description is too short") 