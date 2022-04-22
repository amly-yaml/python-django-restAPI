from django.urls import path
from .views import MovieAPIView, MovieDetailAPI

urlpatterns = [
  path('', MovieAPIView.as_view()), 
  path('<int:pk>/', MovieDetailAPI.as_view()),
]
