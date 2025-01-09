from django.shortcuts import render
from rest_framework import viewsets
from .models import Movie
from .serializers import MovieSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class MovieViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing movies.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(
        operation_summary="List all movies",
        operation_description="Returns a list of all movies in the database",
        responses={200: MovieSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create a new movie",
        operation_description="Creates a new movie entry with the provided data",
        request_body=MovieSerializer,
        responses={201: MovieSerializer()}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Retrieve a specific movie",
        operation_description="Returns the details of a specific movie",
        responses={200: MovieSerializer()}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Update a movie",
        operation_description="Updates all fields of an existing movie",
        request_body=MovieSerializer,
        responses={200: MovieSerializer()}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Partial update a movie",
        operation_description="Updates some fields of an existing movie",
        request_body=MovieSerializer,
        responses={200: MovieSerializer()}
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Delete a movie",
        operation_description="Deletes an existing movie",
        responses={204: "No content"}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
