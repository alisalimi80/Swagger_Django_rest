from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Movie ,Profile

class MovieSerializer(serializers.ModelSerializer):

    casts = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='id'
    )

    writer = serializers.StringRelatedField()

    class Meta:
        model = Movie
        fields = ['id','name', 'time', 'country', 'description','language','casts','writer']


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ['avatar','bio']


class UserSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["id","username","email","first_name","last_name"]

#-----------------------------------------------------------------------------------------------------
#upload file for swagger

class YourSerializer(serializers.Serializer):
   """Your data serializer, define your fields here."""
   link_count = serializers.IntegerField()

#-----------------------------------------------------------------------------------------------------
#upload file serializers
# Serializers define the API representation.

class UploadSerializer(serializers.Serializer):
    file_uploaded = serializers.FileField()
    class Meta:
        fields = ['file_uploaded']