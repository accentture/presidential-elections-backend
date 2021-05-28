#thrird
from rest_framework import serializers

#local
from django.contrib.auth.models import User

#app
from .models import (
    CategoryComment, 
    Comment, 
    CommentOfUser
)
from applications.candidates.models import Candidate

class CreateCommentSerializer(serializers.Serializer):
    email = serializers.CharField()
    candidate_id = serializers.CharField()
    content_comment = serializers.CharField()
    category_comment_id = serializers.IntegerField()

#-----------------------------------------
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name'
        )

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = (
            'id',
            'names',
            'surnames'
        )

class CommentOfUserSerializer(serializers.ModelSerializer):
    candidate = CandidateSerializer()
    user = UserSerializer()

    class Meta:
        model = CommentOfUser
        fields = (
            'id',
            'candidate',
            'user'
        )

#-------------------------------------------------------
class CommentsSerializer(serializers.ModelSerializer):
    comment_of_user = serializers.SerializerMethodField()
    class Meta:
        model = Comment
        fields = (
            'id',
            'content',
            'category_comment',
            'parent',
            'comment_of_user'
        )

    def get_comment_of_user(self, obj): #obj = object of Model
        query = CommentOfUser.objects.filter(comment_id = obj.id)
        comment_of_user_serialized = CommentOfUserSerializer(query, many = True).data
        return comment_of_user_serialized








