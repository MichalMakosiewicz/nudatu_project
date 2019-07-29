from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Movie, Comment
from .serializers import CommentSerializer, MovieSerializer
from rest_framework import generics
from django_filters import rest_framework as filters


class SnippetFilter(filters.FilterSet):
    id_filter = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Comment
        fields = ('movie',)

class MovieViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    permission_classes = [AllowAny]
    queryset = Movie.objects.all()



class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [AllowAny]
    queryset = Comment.objects.all()
    filterset_class = SnippetFilter
