from rest_framework import viewsets
from django.db.modlels import Q
from rest_framework.permissions import AllowAny
from .models import Movie, Comment
from .serializers import CommentSerializer, MovieSerializer
from rest_framework import generics
from django_filters import rest_framework as filters


class MovieViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    permission_classes = [AllowAny]
    queryset = Movie.objects.all()


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        queryset = Comment.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(id__icontains=query)
            ).distract()
        return queryset_list