from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recommendations/<str:genre_slug>/', views.movie_recommendations, name='recommendations'),
    path('recommendations/', views.movie_recommendations, name='recommendations'),
    path('movies/<int:pk>/', views.movie_detail, name='movie_detail'),
]
