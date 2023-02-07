from django.contrib.auth.models import User
from .serializers import MovieSerializer , ProfileSerializer , UserSerializers , YourSerializer
from rest_framework.views import APIView
from .models import Movie , Profile
from rest_framework.response import Response
from rest_framework import status 
from drf_spectacular.utils import extend_schema 


class Movies_view(APIView):

    @extend_schema(description='Show you all movies list',
                    methods=["GET"],
                    responses={200: MovieSerializer},)
    
    def get(self,request):
        query = Movie.objects.all()
        serializers = MovieSerializer(query,many=True)
        return Response (serializers.data)


class Detailmovie(APIView):
    @extend_schema(description='The movie you give ID to',
                    methods=["GET"],
                    responses={200: MovieSerializer},)
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


#-------------------------------------------------------------------------------------------
#upload file for swagger

class FileUploadView(APIView):
    @extend_schema(description='post links file',
                    methods=["POST"],
                    request={
                    'multipart/form-data': {
                        'type': 'object',
                        'properties': {
                            'file': {
                                'type': 'string',
                                'format': 'binary'
                                }
                            }
                        }
                    },
                    responses={202:YourSerializer},
                    )
    def post(self, request):
        file_obj = request.data['file']
        links = file_obj.readlines()
        link_count = 0
        for link in links:
            print(link.decode('utf-8'))
            link_count+=1
        return Response({"Link count":link_count},status=status.HTTP_202_ACCEPTED)

#-------------------------------------------------------------------------------------------
#upload file with django rest viewset

from rest_framework.viewsets import ViewSet
from .serializers import UploadSerializer

# ViewSets define the view behavior.
class UploadViewSet(ViewSet):
    serializer_class = UploadSerializer

    def list(self, request):
        return Response("GET API")

    def create(self, request):
        file_uploaded = request.FILES.get('file_uploaded')
        content_type = file_uploaded.content_type
        response = "POST API and you have uploaded a {} file".format(content_type)
        return Response(response)

