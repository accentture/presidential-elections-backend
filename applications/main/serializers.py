#thrid
from rest_framework import serializers
from rest_framework import exceptions
#django
from django.contrib.auth.models import User

#local
from .models import UserProfile
  

class CreateUserSerializer(serializers.ModelSerializer):
    #user = UserSerializer()
    gender = serializers.CharField()

    class Meta:
        model = User

        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
            'gender',
        )

class LoginUserSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        email = data["email"]
        password = data["password"]

        try:
            user = User.objects.get(email = email, password = password)
            data['user'] = user
            return data
        except:
            data['user'] = {}
            return data
        
        #raise serializers.ValidationError("User Not Found")

class VoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = (
            'vote',
        )

    """
    def create(self,validated_data):

        print('------------------validated data-----------', validated_data)
        userprofile, created = userprofile.objects.get_or_create(**validated_data)
        if not created:
           userprofile.vote='rest'
        # you have to write your own logic i give you just an hint 
        return userprofile
    """


    

