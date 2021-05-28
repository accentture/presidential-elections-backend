#thrid
from rest_framework import serializers

#app
from .models import Candidate

class DataCandidate(serializers.ModelSerializer):
    #photo = serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)
    class Meta:
        model = Candidate
        fields = (
            'id',
            'names',
            'surnames',
            'education',
            'country',
            'career_path',
            'political_party',
            'photo',
            'photo_political_party'
        )



