from django.shortcuts import render, get_object_or_404
from .models import Movie, Genre


def movie_recommendations(request, genre_slug=None):
    """
    Vista pública de recomendación:
    Muestra las mejores películas valoradas, filtradas por género si se proporciona.
    """
    movies = Movie.objects.prefetch_related('genres', 'ratings').all()

    genre = None
    if genre_slug:
        genre = get_object_or_404(Genre, name__iexact=genre_slug)
        movies = movies.filter(genres=genre)

    # Calculate average rating per movie
    movies_with_avg = []
    for movie in movies:
        ratings = movie.ratings.all()
        if ratings:
            avg_rating = sum(r.rating for r in ratings) / len(ratings)
            max_rating = max(r.rating for r in ratings)
        else:
            avg_rating = 0
            max_rating = 0
        movies_with_avg.append({
            'movie': movie,
            'avg_rating': round(avg_rating, 1),
            'max_rating': max_rating,
            'num_ratings': ratings.count(),
        })

    # Sort by average rating descending
    movies_with_avg.sort(key=lambda x: x['avg_rating'], reverse=True)

    all_genres = Genre.objects.prefetch_related('movies').all()

    context = {
        'movies': movies_with_avg,
        'genres': all_genres,
        'selected_genre': genre,
    }
    return render(request, 'movies/recommendations.html', context)


def home(request):
    """Vista de inicio que redirige a recomendaciones."""
    return render(request, 'movies/home.html')
