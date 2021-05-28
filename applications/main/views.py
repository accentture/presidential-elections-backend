#third applications
from rest_framework.views import APIView
from rest_framework.generics import (
    RetrieveAPIView,
    CreateAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView
)
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

#django
from django.contrib.auth.models import User

#local
from .serializers import (
    CreateUserSerializer, 
    LoginUserSerializer,
    VoteSerializer
)
from .models import UserProfile


class CreateUser(CreateAPIView):
    serializer_class = CreateUserSerializer

    def create_user(self, serializer):
        print('-----------------register-------------',
        serializer.validated_data['email'],
        serializer.validated_data['password'])
        user = User.objects.create(
            username = serializer.validated_data['username'],
            first_name = serializer.validated_data['first_name'],
            last_name = serializer.validated_data['last_name'],
            email = serializer.validated_data['email'],
            password = serializer.validated_data['password']
        )
        user.save()
        print('-----------------user---------------', user.email)
        return user

    def create_token(self, user):
        if user :
            token = Token.objects.create(user = user)
        return

    def create_user_profile(self, user, serializer):   
        userprofile = UserProfile(
            user_id = user.id,
            gender = serializer.validated_data['gender']
        )
        userprofile.save()

        return

    def create(self, request, *args, **kwargs):
        serializer = CreateUserSerializer(data = request.data)

        serializer.is_valid(raise_exception = True)

        user = self.create_user(serializer)
        self.create_token(user)
        self.create_user_profile(user, serializer)

        return Response({'message':'Success register'}) 

class LoginUser(CreateAPIView):
    serializer_class = LoginUserSerializer
    def get_user_profile(self, user):
        return UserProfile.objects.filter(user_id = user.id)
        
    def post(self, request, *args, **kwargs):
        serializer = LoginUserSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        
        if user :
            userprofile = self.get_user_profile(user)
            token = Token.objects.get(user = user)

            return Response({
                "message":"Correct authentication", 
                "user_token": token.key,
                "user": {
                    "email":user.email
                },
                "user_profile":{
                    "id":userprofile[0].id,
                    "vote":userprofile[0].vote_id
                }
            })
        else:  
            return Response({"message":"This user doesn't exist" })


class UpdateVote(RetrieveUpdateAPIView):
    serializer_class = VoteSerializer
    authentication_classes = (TokenAuthentication, )
    permision_classes = [IsAuthenticated]
    
    """
    def post(self, request):
        data = request.data #other way to acces to data serialized
        print('-------------------------------data------------------', data)
        return Response({"message":"Favorite candiddate updated successly" })
    """
    
    def get_queryset(self):
        #====================== pretty usefull
        print('--------------request--------------', self.request.data) # data serialized sent
        user_id = self.kwargs['pk'] #pk of url
        print('------------------user---------------', UserProfile.objects.filter(user_id = user_id))

        return UserProfile.objects.all()
    
    


