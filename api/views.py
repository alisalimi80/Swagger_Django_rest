from django.contrib.auth.models import User
from .serializers import MovieSerializer , ProfileSerializer
from rest_framework.views import APIView
from .models import Movie , Profile
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class Movies_view(APIView):
    def get(self,request):
        query = Movie.objects.all()
        serializers = MovieSerializer(query,many=True)
        return Response (serializers.data)


class Profile_view(APIView):
    def get(self,request):
        query = Profile.objects.get(user=request.user)
        serializers = ProfileSerializer(query)
        print(f"{serializers.data}------------------------------------")
        return Response (serializers.data)