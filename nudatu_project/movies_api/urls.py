from django.urls import path, include
from .import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('movies', views.MovieViewSet)
router.register('comment', views.CommentViewSet, basename='Comment')

urlpatterns = [
    path('', include(router.urls)),
]
