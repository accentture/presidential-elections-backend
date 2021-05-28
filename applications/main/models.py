#third
from model_utils.models import TimeStampedModel 

#django
from django.db import models

from django.contrib.auth.models import User
from applications.candidates.models import Candidate

class UserProfile(TimeStampedModel):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    gender = models.CharField(max_length = 10, default = True)
    vote = models.ForeignKey(Candidate, on_delete = models.CASCADE, null = True, blank = True)

    