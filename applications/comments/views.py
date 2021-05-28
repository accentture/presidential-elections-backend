#third
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView 
)
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

#local
from django.contrib.auth.models import User

#app
from applications.candidates.models import Candidate
from .serializers import (
    CreateCommentSerializer, 
    CommentsSerializer,
)
from .models import CommentOfUser, Comment, CategoryComment 


class CreateComment(CreateAPIView):
    serializer_class = CreateCommentSerializer
    authentication_classes = (TokenAuthentication, )
    permision_classes = [IsAuthenticated]
    
    def create_comment(self, serializer):
        print('-------------------serializer-------------------', serializer)
        print('-------------------id-------------------', serializer.validated_data['category_comment_id'])
        comment = Comment(
            content = serializer.validated_data['content_comment'],
            category_comment_id = serializer.validated_data['category_comment_id']
        )
        comment.save()

        return comment

    def create_comments_of_user(self, user, serializer, comment):
        candidate = Candidate.objects.get(id = serializer.validated_data['candidate_id'])

        if candidate:
            comment_of_user = CommentOfUser.objects.create(
                user_id = user.id,
                candidate_id = candidate.id,
                comment_id = comment.id
            )
            comment_of_user.save()
        
            return comment_of_user

        return False

    def create(self, request, *args, **kwargs):
        serializer = CreateCommentSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)

        user = User.objects.get(email = serializer.validated_data['email'])
        if(user):
            comment = self.create_comment(serializer)
            comment_of_user = self.create_comments_of_user(user, serializer, comment)

            if comment_of_user:
                return Response({
                    'message':'Comment created successly',
                    'user':{
                        "id":user.id,
                        "username":user.username,
                        "first_name":user.first_name,
                        "last_name":user.last_name
                    },
                    'comment':{
                        'id':comment.id,
                        'content':comment.content,
                        'category_comment':comment.category_comment_id,
                    }
                }) 

        return Response({'message': 'It is imposible to create comment'})

        

class CommentsPagination(ListAPIView):
    authentication_classes = (TokenAuthentication, )
    permision_classes = [IsAuthenticated]
    serializer_class = CommentsSerializer
    
    def get_queryset(self):
        print('-------------param url-----------', self.kwargs['candidate_id'])
        #candidate_id = self.request.data['candidate_id'] # data of body

        candidate_id = self.kwargs['candidate_id'] 
        category_comment_id = self.kwargs['category_comment_id'] 

        comments_ids = CommentOfUser.objects.filter(candidate_id = candidate_id).values_list('comment_id', flat = True)
        comments = Comment.objects.filter(pk__in=comments_ids, category_comment_id = category_comment_id) 

        return comments



