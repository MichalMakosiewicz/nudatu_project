from rest_framework import serializers
from .models import Movie, Comment, Top


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('name', 'id')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('text', 'author', 'movie')


class TopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Top
        fields = ('total_comments', 'rank')
