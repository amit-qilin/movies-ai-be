from django.core.management.base import BaseCommand
from movies.models import Movie
from datetime import date

class Command(BaseCommand):
    help = 'Loads dummy movie data into the database'

    def handle(self, *args, **kwargs):
        # Delete all existing movies
        Movie.objects.all().delete()

        movies_data = [
            {
                'title': 'The Shawshank Redemption',
                'description': 'Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.',
                'release_date': date(1994, 9, 23),
                'duration': 142,
                'genre': 'Drama',
                'rating': 9.3,
                'director': 'Frank Darabont'
            },
            {
                'title': 'Inception',
                'description': 'A thief who steals corporate secrets through dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O.',
                'release_date': date(2010, 7, 16),
                'duration': 148,
                'genre': 'Sci-Fi',
                'rating': 8.8,
                'director': 'Christopher Nolan'
            },
            {
                'title': 'Pulp Fiction',
                'description': 'The lives of two mob hitmen, a boxer, a gangster and his wife, and a pair of diner bandits intertwine in four tales of violence and redemption.',
                'release_date': date(1994, 10, 14),
                'duration': 154,
                'genre': 'Crime',
                'rating': 8.9,
                'director': 'Quentin Tarantino'
            },
            {
                'title': 'The Dark Knight',
                'description': 'When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.',
                'release_date': date(2008, 7, 18),
                'duration': 152,
                'genre': 'Action',
                'rating': 9.0,
                'director': 'Christopher Nolan'
            },
            {
                'title': 'Forrest Gump',
                'description': 'The presidencies of Kennedy and Johnson, the Vietnam War, the Watergate scandal and other historical events unfold from the perspective of an Alabama man with an IQ of 75.',
                'release_date': date(1994, 7, 6),
                'duration': 142,
                'genre': 'Drama',
                'rating': 8.8,
                'director': 'Robert Zemeckis'
            }
        ]

        for movie_data in movies_data:
            Movie.objects.create(**movie_data)
            self.stdout.write(self.style.SUCCESS(f'Successfully created movie "{movie_data["title"]}"'))

        self.stdout.write(self.style.SUCCESS('Successfully loaded all dummy movies')) 