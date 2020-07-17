from django.shortcuts import render
import requests

API_URL = 'https://ghibliapi.herokuapp.com/'


def movies_list(request):
    try:
        is_cached = ('films' in request.session)
        if not is_cached:
            request.session['films'] = _get_people_in_films(
                requests.get(API_URL + 'films').json())
        films = request.session['films']
        return render(request,
                      'movies/movies_list.html',
                      {'films': films})
    except Exception as error:
        print(error)
        return 'Failed to retrieve data, please try again.'


def _get_people_in_films(films):
    people = requests.get(API_URL + 'people').json()
    people_film = []
    for person in people:
        for f in person['films']:
            people_film.append({
                'id': f.split('films/')[1],
                'name': person['name']
            })
    for film in films:
        film['people'] = []
        for p in people_film:
            if p['id'] == film['id']:
                if p['name'] not in film['people']:
                    film['people'].append(p['name'])
        film['people'] = ', '.join(film['people'])
    return films
