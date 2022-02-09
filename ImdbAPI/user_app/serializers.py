from django.forms import ValidationError
from rest_framework import serializers
from django.contrib.auth.models import User

class RegistrationSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model=User
        fields=['username','email','password','password2']
        extra_kwargs={
            'password':{'write_only':True}
        }

    def save(self, **kwargs):
        username=self.validated_data['username']
        password=self.validated_data['password']
        password2=self.validated_data['password2']
        email=self.validated_data['email']
        
        
        if password2!=password:
            raise serializers.ValidationError("p1 and p2 not same")
        
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("email already exist")
           
        account=User(email=email,username=username)
        account.set_password(password)
        account.save()
        
        return account
        