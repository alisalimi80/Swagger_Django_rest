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
        fields = ['name', 'time', 'country', 'description','language','casts','writer']


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ['user','avatar','bio']
