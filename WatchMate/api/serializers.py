from wsgiref.validate import validator
from django.forms import ValidationError
from rest_framework import serializers
from main.models import Movie
from .validators import check_length


# class MovieSerializer(serializers.Serializer):
#     id=serializers.IntegerField(read_only=True)
#     name=serializers.CharField()
#     description=serializers.CharField(validators=[check_length])
#     active=serializers.BooleanField()

#     def create(self, validated_data):
#        return Movie.objects.create(**validated_data)
    
#     # instance -> old values && validated data -> new values  putting new values in old values 
#     def update(self, instance, validated_data):
#         instance.name=validated_data.get('name')
#         instance.description=validated_data.get('description')
#         instance.active=validated_data.get('active')
#         instance.save()
#         return instance  
    
    
#     # Validators -> Three Types
    
#     # Field Level Validation -> for a particular Filed
#     def validate_name(self,value):
#         if(len(value)>50):
#             raise serializers.ValidationError("Name is too long")
#         else:
#             return value
        
        
#     # Object Level Validation -> for a complete object  when it is submitted 
#     # eg. compare two field in a single object

    
#     def validate(self,data):
#         if data['name']==data['description']:
#               raise serializers.ValidationError("Movie Name and Description should be different.")
#         else:
#             return data  
        
        
#     # validators -> Core Argument Passed to current field above ^ 
#     # like Used above in description for description field that takes value and check it for a certain condition


# With Model Serializer update and create fnuction are provided automatically
# But validators we need to define
class MovieSerializer(serializers.ModelSerializer):

    len_name=serializers.SerializerMethodField()   # Custom serializer Field
    class Meta:
        model=Movie
        fields='__all__'

    def get_len_name(self,object):
        return len(object.name)

    # Field Level Validation -> for a particular Filed
    def validate_name(self,value):
        if(len(value)>50):
            raise serializers.ValidationError("Name is too long")
        else:
            return value
        
        
    # Object Level Validation -> for a complete object  when it is submitted 
    # eg. compare two field in a single object

    
    def validate(self,data):
        if data['name']==data['description']:
              raise serializers.ValidationError("Movie Name and Description should be different.")
        else:
            return data  
