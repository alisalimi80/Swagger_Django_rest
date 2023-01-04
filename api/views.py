from django.contrib.auth.models import User
from .serializers import MovieSerializer
from rest_framework.views import APIView
from .models import Movie
from rest_framework.response import Response




class Movies_view(APIView):

    def get(self,request):

        query = Movie.objects.all()
        serializers = MovieSerializer(query,many=True)
        return Response (serializers.data)





