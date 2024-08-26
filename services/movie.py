from django.db.models import QuerySet

from db.models import Movie, Actor, Genre


def get_movies(
        genres_ids: list | None = None,
        actors_ids: list | None = None
) -> QuerySet:
    movies = Movie.objects.all()

    if genres_ids:
        movies = movies.filter(genres__id__in=genres_ids)
    if actors_ids:
        movies = movies.filter(actors__id__in=actors_ids)
    return movies


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        actors_ids: list | None = None,
        genres_ids: list | None = None
) -> Movie:
    created_movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )

    if actors_ids:
        actors = Actor.objects.filter(id__in=actors_ids)
        created_movie.actors.set(actors)
    if genres_ids:
        genres = Genre.objects.filter(id__in=genres_ids)
        created_movie.genres.set(genres)

    return created_movie