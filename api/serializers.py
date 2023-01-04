from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.HyperlinkedModelSerializer):

    casts = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='id'
    )

    writer = serializers.StringRelatedField()

    class Meta:
        model = Movie
        fields = ['name', 'time', 'country', 'description','language','casts','writer']
    