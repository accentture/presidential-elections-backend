#third
from model_utils.models import TimeStampedModel 

#django
from django.db import models
from django.contrib.auth.models import User

#local
from applications.candidates.models import Candidate

class CategoryComment(models.Model):
    description = models.CharField(max_length = 255)

    def __str__(self):
        return self.description

class Comment(models.Model):
    content = models.TextField()
    category_comment = models.ForeignKey(CategoryComment, on_delete = models.CASCADE)
    parent = models.ForeignKey('self', blank = True, null = True, on_delete = models.CASCADE)

    def __str__(self):
        return self.content

class CommentOfUser(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete = models.CASCADE)
    comment = models.OneToOneField(Comment, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)




    



