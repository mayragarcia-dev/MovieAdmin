from django.core.management.base import BaseCommand
from movies.models import Genre, Person, Movie, Rating


class Command(BaseCommand):
    help = 'Cargar datos de prueba para películas'

    def handle(self, *args, **kwargs):
        # Create genres
        genre_data = [
            ('Acción', 'Películas con escenas de combate y persecuciones'),
            ('Comedia', 'Películas diseñadas para provocar humor y risas'),
            ('Drama', 'Películas con tramas serias y personajes profundos'),
            ('Ciencia Ficción', 'Películas con temas futuristas y tecnológicos'),
        ]
        genres = []
        for name, desc in genre_data:
            genre, created = Genre.objects.get_or_create(name=name, defaults={'description': desc})
            genres.append(genre)
            if created:
                self.stdout.write(f'  [Genre] {name} creado')

        # Create persons
        person_data = [
            ('Ana García', '1985-03-15', 'Española'),
            ('Carlos López', '1990-07-22', 'Mexicana'),
            ('María Torres', '1978-11-30', 'Argentina'),
            ('Pedro Ruiz', '1982-05-10', 'Colombiana'),
            ('Laura Martín', '1995-01-18', 'Española'),
        ]
        persons = []
        for name, birth, nation in person_data:
            person, created = Person.objects.get_or_create(name=name, defaults={'birth_date': birth, 'nationality': nation})
            persons.append(person)
            if created:
                self.stdout.write(f'  [Person] {name} creado')

        # Create movies
        movies = [
            {
                'title': 'El Último Horizonte',
                'description': 'Una historia de supervivencia en un planeta desconocido.',
                'release_date': '2023-06-15',
                'duration': 142,
                'genres': [genres[3]],
                'ratings': [
                    {'person': persons[0], 'rating': 9, 'comment': 'Increíble visualmente.'},
                    {'person': persons[1], 'rating': 8, 'comment': 'Buena trama, ritmo lento.'},
                ],
            },
            {
                'title': 'Risas en la Ciudad',
                'description': 'Un comediante intenta reconstruir su vida.',
                'release_date': '2022-02-14',
                'duration': 105,
                'genres': [genres[1]],
                'ratings': [
                    {'person': persons[2], 'rating': 7, 'comment': 'Divertida pero predecible.'},
                ],
            },
            {
                'title': 'Sombras del Pasado',
                'description': 'Un detective retrocede en su propia historia.',
                'release_date': '2021-10-31',
                'duration': 130,
                'genres': [genres[0], genres[2]],
                'ratings': [
                    {'person': persons[0], 'rating': 8, 'comment': 'Muy bien actuada.'},
                    {'person': persons[3], 'rating': 9, 'comment': 'Una joya del cine.'},
                    {'person': persons[4], 'rating': 7, 'comment': 'Final inesperado.'},
                ],
            },
            {
                'title': 'Galaxiones',
                'description': 'Aventura espacial con efectos especiales impresionantes.',
                'release_date': '2024-01-20',
                'duration': 155,
                'genres': [genres[3], genres[0]],
                'ratings': [
                    {'person': persons[1], 'rating': 10, 'comment': 'Obra maestra absoluta.'},
                    {'person': persons[2], 'rating': 8, 'comment': 'Entretenida de inicio a fin.'},
                ],
            },
            {
                'title': 'Corazón Roto',
                'description': 'Un drama sobre el amor y la pérdida.',
                'release_date': '2020-09-25',
                'duration': 118,
                'genres': [genres[2]],
                'ratings': [
                    {'person': persons[3], 'rating': 6, 'comment': 'Emotiva pero lenta.'},
                ],
            },
            {
                'title': 'Furia Implacable',
                'description': 'Un ex militar busca venganza.',
                'release_date': '2019-07-04',
                'duration': 125,
                'genres': [genres[0]],
                'ratings': [
                    {'person': persons[0], 'rating': 7, 'comment': 'Acción sin parar.'},
                    {'person': persons[4], 'rating': 5, 'comment': 'Demasiado violenta.'},
                ],
            },
            {
                'title': 'Vida de Barrio',
                'description': 'Comedia de errores en un pequeño pueblo.',
                'release_date': '2023-12-01',
                'duration': 98,
                'genres': [genres[1]],
                'ratings': [
                    {'person': persons[2], 'rating': 8, 'comment': 'Muy simpática.'},
                    {'person': persons[1], 'rating': 9, 'comment': 'Mi favorita del año.'},
                ],
            },
            {
                'title': 'El Laboratorio',
                'description': 'Científicos descubren algo que cambiará la humanidad.',
                'release_date': '2022-08-19',
                'duration': 135,
                'genres': [genres[3], genres[2]],
                'ratings': [
                    {'person': persons[0], 'rating': 9, 'comment': 'Inteligente y profunda.'},
                    {'person': persons[3], 'rating': 8, 'comment': 'Ciencia ficción de calidad.'},
                    {'person': persons[4], 'rating': 6, 'comment': 'Un poco confusa.'},
                ],
            },
            {
                'title': 'Amor en París',
                'description': 'Una romance entre dos desconocidos en la ciudad luz.',
                'release_date': '2021-02-14',
                'duration': 110,
                'genres': [genres[1], genres[2]],
                'ratings': [
                    {'person': persons[2], 'rating': 7, 'comment': 'Encantadora.'},
                ],
            },
            {
                'title': 'Operación Trueno',
                'description': 'Un equipo de élite lleva a cabo una misión imposible.',
                'release_date': '2024-05-10',
                'duration': 140,
                'genres': [genres[0], genres[3]],
                'ratings': [
                    {'person': persons[0], 'rating': 10, 'comment': 'La mejor película de acción en años.'},
                    {'person': persons[1], 'rating': 9, 'comment': 'Espectacular en todo sentido.'},
                    {'person': persons[3], 'rating': 8, 'comment': 'Muy bien dirigida.'},
                ],
            },
        ]

        for m in movies:
            movie, created = Movie.objects.get_or_create(
                title=m['title'],
                defaults={
                    'description': m['description'],
                    'release_date': m['release_date'],
                    'duration': m['duration'],
                },
            )
            if created:
                movie.genres.set(m['genres'])
                self.stdout.write(f'  [Movie] {m["title"]} creado')
            else:
                self.stdout.write(f'  [Movie] {m["title"]} ya existía')

            for r in m['ratings']:
                rating, created = Rating.objects.get_or_create(
                    movie=movie,
                    person=r['person'],
                    defaults={'rating': r['rating'], 'comment': r['comment']},
                )
                if created:
                    self.stdout.write(f'    [Rating] {movie.title} - {r["person"].name}: {r["rating"]}/10')

        self.stdout.write(self.style.SUCCESS('\n¡Datos de prueba cargados correctamente!'))
