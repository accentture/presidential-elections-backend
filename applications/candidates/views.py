
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status

#serializers
from .serializers import DataCandidate

#models
from .models import Candidate

class RenderDataCandidate(ListAPIView):
    serializer_class = DataCandidate
    #queryset = Candidate.objects.all()

    
    #===================other interesting way to get data from server, but using  APIView
    def get(self, request, *args, **kwargs):

        candidates = Candidate.objects.all()
        for candidate in candidates:
            candidate.photo.url_options.update({'secure':True}) #to get secure url
            candidate.photo = candidate.photo.url

        serializer = DataCandidate(candidates, many=True, context={"request":request})

        return Response(serializer.data, status=status.HTTP_200_OK)
    
        


    

