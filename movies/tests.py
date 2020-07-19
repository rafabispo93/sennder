from django.test import TestCase
from django.urls import reverse
from movies import views

'''
    This unit test is covering if the view returns the HTML correctly,
    also is testing if the session is set to expire every 1 minute (time to perform new requests to the external API)
    and if the external request is being cached for returning data within the 1 minute time length.
    Finally, it's testing if the method that gets films is returning the films with its people.

'''

class MoviesTest(TestCase):

    def test_movies_list_view(self):

        self.assertIsNone(self.client.session.get('films'))

        url = reverse(views.movies_list)
        resp = self.client.get(url)

        self.assertEqual(self.client.session.get_expiry_age(), 60) # Test if the request is cached every 1 minute
        self.assertIsNotNone(self.client.session.get('films'))
        self.assertEqual(resp.status_code, 200)
        self.assertIsNotNone(resp.content)

    def test_get_films(self):

        films = views._get_films_ordered_by_most_recent()
        self.assertIsNot(len(films), 0)
        for film in films:
            self.assertTrue('people' in film.keys())