from django.contrib.auth.models import User
from .serializers import MovieSerializer , ProfileSerializer , UserSerializers
from rest_framework.views import APIView
from .models import Movie , Profile
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema
from rest_framework.generics import GenericAPIView

class Movies_view(GenericAPIView):
    serializer_class = MovieSerializer

    @extend_schema(description='Show you all movies list',
                    methods=["GET"],
                    responses={200: MovieSerializer},)
    
    def get(self,request):
        query = Movie.objects.all()
        serializers = MovieSerializer(query,many=True)
        return Response (serializers.data)


class Detailmovie(GenericAPIView):
    serializer_class = MovieSerializer
    @extend_schema(description='The movie you give ID to',
                    methods=["GET"],)
    def get(self,request,pk):
        query = Movie.objects.get(id=pk)
        serializer = MovieSerializer(query)
        return Response(serializer.data)



class Profile_view(APIView):
    def get(self,request):
        if request.user.is_authenticated:
            query = Profile.objects.get(user=request.user)
            user_query = User.objects.get(id=request.user.id)
            user_serializer = UserSerializers(user_query)
            serializers = ProfileSerializer(query)
            print(f"{serializers.data}------------------------------------")
            return Response ({
                "profile":serializers.data,
                "user_detail" : user_serializer.data})
        else:
            content = {'please login': 'you are not authenticate'}
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)
            