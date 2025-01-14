from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('', views.MovieViewSet, basename='movie')

app_name = 'movies'

urlpatterns = [
    path('', include(router.urls)),
] 