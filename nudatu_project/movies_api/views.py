from django.db.models import Q
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Movie, Comment, Top
from .serializers import CommentSerializer, MovieSerializer, TopSerializer
from rest_framework import generics
from django_filters import rest_framework as filters


class MovieViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    permission_classes = [AllowAny]
    queryset = Movie.objects.all()


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        queryset_list = Comment.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(movie__id__icontains=query)
            ).distinct()
        return queryset_list

class TopViewSet(viewsets.ModelViewSet):
    serializer_class = TopSerializer
    permission_classes = [AllowAny]
    queryset = Top.objects.all()
