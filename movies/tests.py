from django.test import TestCase, RequestFactory
from django.urls import reverse
from movies import views
from django.contrib.sessions.middleware import SessionMiddleware


class MoviesTest(TestCase):

    def test_movies_list_view(self):

        url = reverse(views.movies_list)
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertIsNotNone(resp.content)

    def test_get_films(self):

        # request = RequestFactory().get('http://localhost:8000/movies/')
        # middleware = SessionMiddleware()
        # middleware.process_request(request)
        # request.session.save()
        # response = views.movies_list(request)
        films = views._get_films_ordered_by_most_recent()
        self.assertIsNot(len(films), 0)
        for film in films:
            self.assertTrue('people' in film.keys())